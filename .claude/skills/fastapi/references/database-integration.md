# Database Integration with SQLAlchemy

This guide covers integrating SQLAlchemy with FastAPI for database operations.

## Table of Contents
- Setup and Configuration
- Database Models
- Database Session Management
- CRUD Operations
- Migrations with Alembic
- Async SQLAlchemy

## Setup and Configuration

### Install Dependencies

```bash
pip install sqlalchemy alembic psycopg2-binary
```

For async support:
```bash
pip install sqlalchemy[asyncio] aiosqlite  # For SQLite
pip install sqlalchemy[asyncio] asyncpg    # For PostgreSQL
```

### Database Configuration

**app/core/config.py**
```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # SQLite (for development)
    DATABASE_URL: str = "sqlite:///./app.db"

    # PostgreSQL (for production)
    # DATABASE_URL: str = "postgresql://user:password@localhost/dbname"

    # PostgreSQL Async
    # DATABASE_URL: str = "postgresql+asyncpg://user:password@localhost/dbname"

    class Config:
        env_file = ".env"

settings = Settings()
```

### Database Connection Setup

**app/db/database.py**
```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Create engine
engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in settings.DATABASE_URL else {},
)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Dependency for getting DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

## Database Models

### Basic Model Example

**app/models/item.py**
```python
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from sqlalchemy.sql import func
from app.db.database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, index=True)
    description = Column(String(500), nullable=True)
    price = Column(Float, nullable=False)
    tax = Column(Float, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
```

### Relationships

**app/models/user.py**
```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String)

    # One-to-many relationship
    items = relationship("Item", back_populates="owner")

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"))

    # Many-to-one relationship
    owner = relationship("User", back_populates="items")
```

### Many-to-Many Relationships

```python
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

# Association table
item_tags = Table(
    "item_tags",
    Base.metadata,
    Column("item_id", Integer, ForeignKey("items.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tags.id"), primary_key=True),
)

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    tags = relationship("Tag", secondary=item_tags, back_populates="items")

class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    items = relationship("Item", secondary=item_tags, back_populates="tags")
```

### Create Tables

**app/db/init_db.py**
```python
from app.db.database import engine, Base
from app.models import item, user  # Import all models

def create_tables():
    """Create all tables in the database"""
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_tables()
    print("Tables created successfully!")
```

## Database Session Management

### Using Dependency Injection

**In endpoints:**
```python
from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.database import get_db

@router.get("/items/")
async def read_items(db: Session = Depends(get_db)):
    items = db.query(Item).all()
    return items
```

### Context Manager Pattern

```python
from app.db.database import SessionLocal

def some_function():
    with SessionLocal() as db:
        items = db.query(Item).all()
        return items
```

## CRUD Operations

### Create CRUD Module

**app/crud/item.py**
```python
from sqlalchemy.orm import Session
from app.models.item import Item
from app.schemas.item import ItemCreate, ItemUpdate

def get_item(db: Session, item_id: int):
    """Get a single item by ID"""
    return db.query(Item).filter(Item.id == item_id).first()

def get_items(db: Session, skip: int = 0, limit: int = 100):
    """Get multiple items with pagination"""
    return db.query(Item).offset(skip).limit(limit).all()

def get_items_by_owner(db: Session, owner_id: int):
    """Get items filtered by owner"""
    return db.query(Item).filter(Item.owner_id == owner_id).all()

def create_item(db: Session, item: ItemCreate, owner_id: int = None):
    """Create a new item"""
    db_item = Item(**item.model_dump(), owner_id=owner_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_item(db: Session, item_id: int, item: ItemUpdate):
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

def delete_item(db: Session, item_id: int):
    """Delete an item"""
    db_item = get_item(db, item_id)
    if db_item:
        db.delete(db_item)
        db.commit()
        return True
    return False

def search_items(db: Session, search: str):
    """Search items by name"""
    return db.query(Item).filter(Item.name.contains(search)).all()
```

### Using CRUD in Endpoints

**app/api/v1/endpoints/items.py**
```python
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.crud import item as crud_item
from app.schemas.item import Item, ItemCreate, ItemUpdate

router = APIRouter()

@router.get("/", response_model=List[Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Retrieve items"""
    items = crud_item.get_items(db, skip=skip, limit=limit)
    return items

@router.get("/{item_id}", response_model=Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    """Get item by ID"""
    db_item = crud_item.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.post("/", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    """Create new item"""
    return crud_item.create_item(db=db, item=item)

@router.put("/{item_id}", response_model=Item)
def update_item(item_id: int, item: ItemUpdate, db: Session = Depends(get_db)):
    """Update item"""
    db_item = crud_item.update_item(db, item_id=item_id, item=item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    """Delete item"""
    success = crud_item.delete_item(db, item_id=item_id)
    if not success:
        raise HTTPException(status_code=404, detail="Item not found")
```

### Pydantic Schema for ORM

**app/schemas/item.py**
```python
from pydantic import BaseModel, ConfigDict
from datetime import datetime

class ItemBase(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

class ItemCreate(ItemBase):
    pass

class ItemUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    tax: float | None = None

class Item(ItemBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)  # Enable ORM mode
```

## Migrations with Alembic

### Initialize Alembic

```bash
alembic init alembic
```

### Configure Alembic

**alembic/env.py**
```python
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# Import your Base and models
from app.db.database import Base
from app.core.config import settings
import app.models.item  # Import all models
import app.models.user

# this is the Alembic Config object
config = context.config

# Set database URL from settings
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)

# Set target metadata
target_metadata = Base.metadata

# ... rest of the file
```

### Create Migration

```bash
# Auto-generate migration from models
alembic revision --autogenerate -m "Create items table"

# Apply migrations
alembic upgrade head

# Rollback one version
alembic downgrade -1
```

## Async SQLAlchemy

### Async Database Setup

**app/db/database.py**
```python
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Async engine
engine = create_async_engine(settings.DATABASE_URL, echo=True)

# Async session factory
AsyncSessionLocal = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

# Async dependency
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
```

### Async CRUD Operations

**app/crud/item.py**
```python
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.item import Item
from app.schemas.item import ItemCreate

async def get_item(db: AsyncSession, item_id: int):
    """Get item by ID (async)"""
    result = await db.execute(select(Item).where(Item.id == item_id))
    return result.scalar_one_or_none()

async def get_items(db: AsyncSession, skip: int = 0, limit: int = 100):
    """Get items with pagination (async)"""
    result = await db.execute(select(Item).offset(skip).limit(limit))
    return result.scalars().all()

async def create_item(db: AsyncSession, item: ItemCreate):
    """Create item (async)"""
    db_item = Item(**item.model_dump())
    db.add(db_item)
    await db.commit()
    await db.refresh(db_item)
    return db_item
```

### Async Endpoints

```python
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db
from app.crud import item as crud_item

router = APIRouter()

@router.get("/{item_id}")
async def read_item(item_id: int, db: AsyncSession = Depends(get_db)):
    """Async endpoint"""
    item = await crud_item.get_item(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
```

## Best Practices

1. **Use ORM models for database**, Pydantic models for validation
2. **Separate CRUD operations** into dedicated modules
3. **Use dependency injection** for database sessions
4. **Always close sessions** (handled automatically with `Depends`)
5. **Use migrations** for schema changes (Alembic)
6. **Add indexes** on frequently queried fields
7. **Use relationships** instead of manual joins when possible
8. **Handle database errors** with try-except blocks
9. **Use transactions** for multi-step operations
10. **Consider async** for high-concurrency applications
