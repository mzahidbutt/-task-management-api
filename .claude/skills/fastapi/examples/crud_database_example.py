"""
Complete FastAPI CRUD + Database Integration Example

This standalone example demonstrates:
1. SQLAlchemy database setup
2. Database models
3. Pydantic schemas
4. CRUD operations
5. FastAPI endpoints with database integration
6. Full Create, Read, Update, Delete operations

To run this example:
1. Install dependencies: pip install fastapi uvicorn sqlalchemy
2. Run the server: python crud_database_example.py
3. Visit http://localhost:8000/docs to try the API
"""

from typing import List, Optional
from datetime import datetime

# FastAPI imports
from fastapi import FastAPI, Depends, HTTPException, status, Query
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# SQLAlchemy imports
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.sql import func

# Pydantic imports
from pydantic import BaseModel, Field, ConfigDict


# ============================================================================
# DATABASE SETUP
# ============================================================================

DATABASE_URL = "sqlite:///./items_example.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},  # Needed for SQLite
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """Database session dependency"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ============================================================================
# DATABASE MODEL
# ============================================================================

class Item(Base):
    """SQLAlchemy Item model"""
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, index=True)
    description = Column(String(500), nullable=True)
    price = Column(Float, nullable=False)
    tax = Column(Float, nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


# ============================================================================
# PYDANTIC SCHEMAS
# ============================================================================

class ItemBase(BaseModel):
    """Base schema with common item attributes"""
    name: str = Field(..., min_length=1, max_length=100, description="Item name")
    description: str | None = Field(None, max_length=500, description="Item description")
    price: float = Field(..., gt=0, description="Item price (must be positive)")
    tax: float | None = Field(None, ge=0, le=100, description="Tax percentage (0-100)")


class ItemCreate(ItemBase):
    """Schema for creating a new item"""
    pass


class ItemUpdate(BaseModel):
    """Schema for updating an item (all fields optional)"""
    name: str | None = Field(None, min_length=1, max_length=100)
    description: str | None = Field(None, max_length=500)
    price: float | None = Field(None, gt=0)
    tax: float | None = Field(None, ge=0, le=100)


class ItemResponse(ItemBase):
    """Schema for item response (includes ID and metadata)"""
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime | None

    model_config = ConfigDict(from_attributes=True)


# ============================================================================
# CRUD OPERATIONS
# ============================================================================

def create_item(db: Session, item: ItemCreate) -> Item:
    """Create a new item"""
    db_item = Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_item(db: Session, item_id: int) -> Optional[Item]:
    """Get a single item by ID"""
    return db.query(Item).filter(Item.id == item_id).first()


def get_items(db: Session, skip: int = 0, limit: int = 100) -> List[Item]:
    """Get multiple items with pagination"""
    return db.query(Item).offset(skip).limit(limit).all()


def get_active_items(db: Session, skip: int = 0, limit: int = 100) -> List[Item]:
    """Get only active items"""
    return db.query(Item).filter(Item.is_active == True).offset(skip).limit(limit).all()


def search_items(db: Session, search: str) -> List[Item]:
    """Search items by name"""
    return db.query(Item).filter(Item.name.contains(search)).all()


def update_item(db: Session, item_id: int, item: ItemUpdate) -> Optional[Item]:
    """Update an existing item"""
    db_item = get_item(db, item_id)
    if not db_item:
        return None

    update_data = item.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_item, field, value)

    db.commit()
    db.refresh(db_item)
    return db_item


def delete_item(db: Session, item_id: int) -> bool:
    """Delete an item"""
    db_item = get_item(db, item_id)
    if not db_item:
        return False

    db.delete(db_item)
    db.commit()
    return True


def deactivate_item(db: Session, item_id: int) -> Optional[Item]:
    """Soft delete - mark as inactive"""
    db_item = get_item(db, item_id)
    if not db_item:
        return None

    db_item.is_active = False
    db.commit()
    db.refresh(db_item)
    return db_item


# ============================================================================
# FASTAPI APPLICATION
# ============================================================================

app = FastAPI(
    title="FastAPI CRUD + Database Example",
    description="Complete example demonstrating CRUD operations with SQLAlchemy",
    version="1.0.0",
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Create database tables on startup
@app.on_event("startup")
def startup_event():
    """Create database tables"""
    Base.metadata.create_all(bind=engine)
    print("Database tables created!")


# ============================================================================
# API ENDPOINTS
# ============================================================================

@app.get("/")
def root():
    """Root endpoint"""
    return {
        "message": "FastAPI CRUD + Database Example",
        "docs": "/docs",
        "endpoints": {
            "create": "POST /items/",
            "list": "GET /items/",
            "get": "GET /items/{item_id}",
            "update": "PUT /items/{item_id}",
            "delete": "DELETE /items/{item_id}",
            "search": "GET /items/search/?q=searchterm",
        }
    }


@app.get("/items/", response_model=List[ItemResponse], tags=["Items"])
def read_items(
    skip: int = Query(0, ge=0, description="Number of items to skip"),
    limit: int = Query(100, ge=1, le=1000, description="Maximum items to return"),
    active_only: bool = Query(False, description="Return only active items"),
    db: Session = Depends(get_db),
):
    """
    Retrieve all items with pagination.

    Example: GET /items/?skip=0&limit=10&active_only=true
    """
    if active_only:
        items = get_active_items(db, skip=skip, limit=limit)
    else:
        items = get_items(db, skip=skip, limit=limit)
    return items


@app.get("/items/search/", response_model=List[ItemResponse], tags=["Items"])
def search_items_endpoint(
    q: str = Query(..., min_length=1, description="Search query"),
    db: Session = Depends(get_db),
):
    """
    Search items by name.

    Example: GET /items/search/?q=laptop
    """
    items = search_items(db, search=q)
    return items


@app.get("/items/{item_id}", response_model=ItemResponse, tags=["Items"])
def read_item(item_id: int, db: Session = Depends(get_db)):
    """
    Get a specific item by ID.

    Example: GET /items/1
    """
    db_item = get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found"
        )
    return db_item


@app.post("/items/", response_model=ItemResponse, status_code=status.HTTP_201_CREATED, tags=["Items"])
def create_new_item(item: ItemCreate, db: Session = Depends(get_db)):
    """
    Create a new item.

    Example:
    ```json
    {
        "name": "Laptop",
        "description": "Gaming laptop",
        "price": 1299.99,
        "tax": 10.5
    }
    ```
    """
    db_item = create_item(db=db, item=item)
    return db_item


@app.put("/items/{item_id}", response_model=ItemResponse, tags=["Items"])
def update_existing_item(
    item_id: int,
    item: ItemUpdate,
    db: Session = Depends(get_db),
):
    """
    Update an existing item.

    Example: PUT /items/1
    ```json
    {
        "price": 1199.99,
        "description": "Updated description"
    }
    ```
    """
    db_item = update_item(db, item_id=item_id, item=item)
    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found"
        )
    return db_item


@app.patch("/items/{item_id}", response_model=ItemResponse, tags=["Items"])
def partial_update_item(
    item_id: int,
    item: ItemUpdate,
    db: Session = Depends(get_db),
):
    """
    Partially update an item (only provided fields).

    Example: PATCH /items/1
    ```json
    {
        "price": 999.99
    }
    ```
    """
    db_item = update_item(db, item_id=item_id, item=item)
    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found"
        )
    return db_item


@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Items"])
def delete_existing_item(item_id: int, db: Session = Depends(get_db)):
    """
    Delete an item permanently.

    Example: DELETE /items/1
    """
    success = delete_item(db, item_id=item_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found"
        )
    return None


@app.post("/items/{item_id}/deactivate", response_model=ItemResponse, tags=["Items"])
def deactivate_existing_item(item_id: int, db: Session = Depends(get_db)):
    """
    Soft delete - mark item as inactive.

    Example: POST /items/1/deactivate
    """
    db_item = deactivate_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found"
        )
    return db_item


# ============================================================================
# RUN THE APPLICATION
# ============================================================================

if __name__ == "__main__":
    print("=" * 80)
    print("FastAPI CRUD + Database Integration Example")
    print("=" * 80)
    print("\nStarting server...")
    print("API Documentation: http://localhost:8000/docs")
    print("Alternative Docs: http://localhost:8000/redoc")
    print("\nPress CTRL+C to stop the server")
    print("=" * 80)

    uvicorn.run(app, host="0.0.0.0", port=8000)
