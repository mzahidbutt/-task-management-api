# FastAPI Project Structure Best Practices

This guide explains how to organize FastAPI projects for maintainability and scalability.

## Table of Contents
- Small Project Structure
- Medium Project Structure
- Large Project Structure
- Module Organization
- Configuration Management
- Best Practices

## Small Project Structure

For simple APIs (< 5 endpoints, no database):

```
project/
├── main.py              # Application entry point
├── requirements.txt     # Dependencies
└── .env                 # Environment variables
```

**main.py:**
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```

## Medium Project Structure

For applications with 5-20 endpoints, basic features:

```
project/
├── main.py                 # Application entry point
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── api.py      # Router aggregator
│   │       └── endpoints/
│   │           ├── __init__.py
│   │           ├── items.py
│   │           └── users.py
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py       # Configuration
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── item.py
│   │   └── user.py
│   ├── crud/               # Database operations
│   │   ├── __init__.py
│   │   ├── item.py
│   │   └── user.py
│   └── models/             # SQLAlchemy models
│       ├── __init__.py
│       ├── item.py
│       └── user.py
├── tests/
│   ├── __init__.py
│   ├── test_items.py
│   └── test_users.py
├── requirements.txt
├── .env
└── README.md
```

## Large Project Structure

For complex applications with many features:

```
project/
├── main.py
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── dependencies.py     # Shared dependencies
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── api.py
│   │       └── endpoints/
│   │           ├── __init__.py
│   │           ├── auth.py
│   │           ├── users.py
│   │           ├── items.py
│   │           └── orders.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── security.py         # Authentication/authorization
│   │   ├── logging.py          # Logging configuration
│   │   └── exceptions.py       # Custom exceptions
│   ├── db/
│   │   ├── __init__.py
│   │   ├── database.py         # Database connection
│   │   └── init_db.py          # Database initialization
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── item.py
│   │   └── order.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── item.py
│   │   ├── order.py
│   │   └── token.py
│   ├── crud/
│   │   ├── __init__.py
│   │   ├── base.py             # Base CRUD class
│   │   ├── user.py
│   │   ├── item.py
│   │   └── order.py
│   ├── services/               # Business logic
│   │   ├── __init__.py
│   │   ├── email.py
│   │   └── payment.py
│   ├── utils/                  # Utility functions
│   │   ├── __init__.py
│   │   └── helpers.py
│   └── middleware/             # Custom middleware
│       ├── __init__.py
│       └── timing.py
├── alembic/                    # Database migrations
│   ├── versions/
│   └── env.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py            # Pytest fixtures
│   ├── api/
│   │   └── test_items.py
│   ├── crud/
│   │   └── test_item.py
│   └── utils/
│       └── test_helpers.py
├── scripts/                    # Utility scripts
│   └── seed_db.py
├── requirements.txt
├── requirements-dev.txt        # Development dependencies
├── .env
├── .env.example
├── .gitignore
├── alembic.ini
├── pytest.ini
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Module Organization

### API Endpoints (`app/api/v1/endpoints/`)

Each endpoint file should focus on one resource:

**items.py:**
```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.schemas.item import Item, ItemCreate, ItemUpdate
from app.crud.item import crud_item

router = APIRouter()

@router.get("/", response_model=List[Item])
def read_items(db: Session = Depends(get_db)):
    return crud_item.get_multi(db)

@router.post("/", response_model=Item)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    return crud_item.create(db, obj_in=item)
```

### Router Aggregator (`app/api/v1/api.py`)

Combine all endpoint routers:

```python
from fastapi import APIRouter
from app.api.v1.endpoints import items, users, orders

api_router = APIRouter()

api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(orders.router, prefix="/orders", tags=["orders"])
```

### Main Application (`main.py`)

Keep it minimal:

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.api import api_router
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
async def root():
    return {"message": "API is running"}
```

### Schemas (`app/schemas/`)

Three schemas per resource:

```python
from pydantic import BaseModel

class ItemBase(BaseModel):
    """Shared properties"""
    name: str
    description: str | None = None
    price: float

class ItemCreate(ItemBase):
    """Properties to receive on creation"""
    pass

class ItemUpdate(BaseModel):
    """Properties to receive on update (all optional)"""
    name: str | None = None
    description: str | None = None
    price: float | None = None

class Item(ItemBase):
    """Properties to return to client"""
    id: int

    model_config = ConfigDict(from_attributes=True)
```

### CRUD (`app/crud/`)

Reusable database operations:

**base.py:**
```python
from typing import Generic, TypeVar, Type, List, Optional
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.db.database import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get(self, db: Session, id: int) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.id == id).first()

    def get_multi(self, db: Session, skip: int = 0, limit: int = 100) -> List[ModelType]:
        return db.query(self.model).offset(skip).limit(limit).all()

    def create(self, db: Session, obj_in: CreateSchemaType) -> ModelType:
        obj_data = obj_in.model_dump()
        db_obj = self.model(**obj_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, db_obj: ModelType, obj_in: UpdateSchemaType) -> ModelType:
        update_data = obj_in.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_obj, field, value)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, id: int) -> Optional[ModelType]:
        obj = self.get(db, id)
        if obj:
            db.delete(obj)
            db.commit()
        return obj
```

**item.py:**
```python
from app.crud.base import CRUDBase
from app.models.item import Item
from app.schemas.item import ItemCreate, ItemUpdate

class CRUDItem(CRUDBase[Item, ItemCreate, ItemUpdate]):
    """Custom methods for items"""
    def get_by_name(self, db: Session, name: str):
        return db.query(Item).filter(Item.name == name).first()

crud_item = CRUDItem(Item)
```

## Configuration Management

### Environment-Based Configuration

**app/core/config.py:**
```python
from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    # API
    PROJECT_NAME: str = "My API"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"

    # CORS
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000"]

    # Database
    DATABASE_URL: str

    # Security
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Environment
    ENVIRONMENT: str = "development"

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
```

**.env:**
```
PROJECT_NAME=My FastAPI Project
DATABASE_URL=postgresql://user:password@localhost/dbname
SECRET_KEY=your-secret-key-here
ENVIRONMENT=development
```

## Best Practices

### 1. Versioning

Always version your API:
```python
# Good
app.include_router(api_router, prefix="/api/v1")

# When making breaking changes, create v2
app.include_router(api_v2_router, prefix="/api/v2")
```

### 2. Dependency Injection

Use FastAPI's dependency system:
```python
from fastapi import Depends

def get_current_user(token: str = Depends(oauth2_scheme)):
    # Validate token and return user
    return user

@router.get("/me")
def read_user_me(current_user: User = Depends(get_current_user)):
    return current_user
```

### 3. Separate Business Logic

Keep endpoints thin, move logic to services:
```python
# app/services/order.py
class OrderService:
    def create_order(self, db: Session, user_id: int, items: List[int]):
        # Complex business logic here
        pass

# app/api/endpoints/orders.py
@router.post("/")
def create_order(user_id: int, items: List[int], db: Session = Depends(get_db)):
    order_service = OrderService()
    return order_service.create_order(db, user_id, items)
```

### 4. Error Handling

Create custom exceptions:
```python
# app/core/exceptions.py
class ItemNotFoundError(HTTPException):
    def __init__(self, item_id: int):
        super().__init__(status_code=404, detail=f"Item {item_id} not found")

# Usage
@router.get("/{item_id}")
def read_item(item_id: int, db: Session = Depends(get_db)):
    item = crud_item.get(db, item_id)
    if not item:
        raise ItemNotFoundError(item_id)
    return item
```

### 5. Testing Structure

Mirror your app structure:
```
tests/
├── api/
│   └── v1/
│       └── test_items.py
├── crud/
│   └── test_item.py
└── conftest.py
```

### 6. Documentation

Document your endpoints:
```python
@router.post("/", response_model=Item, status_code=201)
def create_item(
    item: ItemCreate,
    db: Session = Depends(get_db),
):
    """
    Create a new item.

    - **name**: Item name (required)
    - **description**: Optional description
    - **price**: Item price (must be positive)
    """
    return crud_item.create(db, obj_in=item)
```

## When to Use Each Structure

- **Small**: Quick prototypes, learning, < 5 endpoints
- **Medium**: Most applications, 5-20 endpoints, standard CRUD
- **Large**: Complex applications, microservices, multiple teams

Start small and refactor as needed!
