---
name: fastapi
description: Comprehensive FastAPI development skill for building REST APIs from basics to production-ready applications. Use this skill when working with FastAPI projects including (1) Creating new FastAPI projects, (2) Building CRUD REST APIs, (3) Implementing request/response validation with Pydantic, (4) Integrating databases with SQLAlchemy, (5) Structuring projects following best practices, (6) Customizing API documentation, (7) Writing tests, or any other FastAPI development tasks.
---

# FastAPI Development Skill

Build production-ready REST APIs with FastAPI, from Hello World to professional applications.

## Overview

This skill provides comprehensive guidance for FastAPI development, including:

- Project initialization and structure
- CRUD API development patterns
- Database integration with SQLAlchemy
- Request/response validation with Pydantic
- API documentation customization
- Testing strategies
- Best practices for maintainable code

## Quick Start

### Create a New FastAPI Project

Use the bundled template to start a new project:

```bash
# Using the initialization script
python scripts/init_project.py my-api

# Or copy the template manually
cp -r assets/project-template my-api
cd my-api
pip install -r requirements.txt
cp .env.example .env
fastapi dev main.py
```

The template includes:
- Professional project structure
- Complete CRUD example (items API)
- Pydantic schemas for validation
- Configuration management
- Example tests
- Documentation setup

### Access Your API

Once running:
- API: http://localhost:8000
- Interactive docs: http://localhost:8000/docs
- Alternative docs: http://localhost:8000/redoc

## Development Workflow

### Level 1: Hello World to Basic API

Start with the simplest FastAPI application:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

Run with: `fastapi dev main.py`

**Next steps:**
1. Add path parameters: `@app.get("/items/{item_id}")`
2. Add query parameters: `async def read_items(skip: int = 0, limit: int = 10)`
3. Add request body with Pydantic models

### Level 2: CRUD REST API

Build a complete CRUD API with proper structure.

**Key concepts:**
- Use Pydantic models for request/response validation
- Implement all HTTP methods (GET, POST, PUT, PATCH, DELETE)
- Return appropriate status codes
- Handle errors with HTTPException

See **references/crud-patterns.md** for:
- Standard CRUD endpoint structures
- Pagination patterns
- Filtering and sorting
- Error handling strategies
- Validation patterns
- Bulk operations

**Example endpoint structure:**
```python
@router.get("/", response_model=List[Item])
@router.get("/{item_id}", response_model=Item)
@router.post("/", response_model=Item, status_code=201)
@router.put("/{item_id}", response_model=Item)
@router.patch("/{item_id}", response_model=Item)
@router.delete("/{item_id}", status_code=204)
```

### Level 3: Professional Project Structure

Organize your code for maintainability and scalability.

See **references/project-structure.md** for:
- Small, medium, and large project structures
- Module organization patterns
- Dependency injection
- Separating business logic
- Configuration management

**Recommended structure:**
```
project/
├── main.py              # Entry point
├── app/
│   ├── api/v1/         # API routes
│   ├── core/           # Config, security
│   ├── crud/           # Database operations
│   ├── models/         # SQLAlchemy models
│   └── schemas/        # Pydantic schemas
└── tests/              # Test files
```

### Level 4: Database Integration

Add persistent storage with SQLAlchemy.

See **references/database-integration.md** for:
- Database setup and configuration
- Creating SQLAlchemy models
- Database session management
- CRUD operations with database
- Migrations with Alembic
- Async SQLAlchemy patterns

**Database workflow:**
1. Install dependencies: `sqlalchemy`, `alembic`
2. Configure database URL in `.env`
3. Create SQLAlchemy models in `app/models/`
4. Set up database connection in `app/db/database.py`
5. Implement CRUD operations in `app/crud/`
6. Use dependency injection for database sessions

### Level 5: API Documentation

Customize and enhance your API documentation.

See **references/api-documentation.md** for:
- OpenAPI customization
- Endpoint documentation with docstrings
- Response model documentation
- Organizing endpoints with tags
- Security documentation
- Documentation best practices

**Key practices:**
- Add descriptive docstrings to endpoints
- Use `response_model` for type safety
- Document parameters with `Field`, `Path`, `Query`
- Organize endpoints with tags
- Include examples in schemas
- Document error responses

## Common Tasks

### Add a New Endpoint

1. Create schema in `app/schemas/`:
```python
class ItemCreate(BaseModel):
    name: str
    price: float
```

2. Create endpoint in `app/api/v1/endpoints/`:
```python
@router.post("/", response_model=Item)
async def create_item(item: ItemCreate):
    return {"id": 1, **item.model_dump()}
```

3. Register router in `app/api/v1/api.py`:
```python
api_router.include_router(items.router, prefix="/items", tags=["items"])
```

### Add Database Support

1. Install: `pip install sqlalchemy alembic`

2. Create model in `app/models/item.py`:
```python
class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
```

3. Create CRUD operations in `app/crud/item.py`:
```python
def get_item(db: Session, item_id: int):
    return db.query(Item).filter(Item.id == item_id).first()
```

4. Use in endpoint:
```python
@router.get("/{item_id}")
def read_item(item_id: int, db: Session = Depends(get_db)):
    item = crud_item.get_item(db, item_id)
    if not item:
        raise HTTPException(status_code=404)
    return item
```

### Add Input Validation

Use Pydantic's validation features:

```python
from pydantic import BaseModel, Field, field_validator

class ItemCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    price: float = Field(..., gt=0)

    @field_validator("name")
    @classmethod
    def name_must_not_be_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Name cannot be empty")
        return v.strip()
```

### Handle Errors

Create custom exception classes:

```python
class ItemNotFoundError(HTTPException):
    def __init__(self, item_id: int):
        super().__init__(
            status_code=404,
            detail=f"Item {item_id} not found"
        )

# Usage
@router.get("/{item_id}")
def read_item(item_id: int):
    if item_id not in items:
        raise ItemNotFoundError(item_id)
    return items[item_id]
```

### Add Tests

Use pytest with FastAPI's TestClient:

```python
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_item():
    response = client.post("/api/v1/items/", json={
        "name": "Test", "price": 10.99
    })
    assert response.status_code == 201
    assert response.json()["name"] == "Test"
```

## Reference Documentation

The skill includes comprehensive reference guides:

- **crud-patterns.md** - CRUD operations, pagination, filtering, error handling
- **database-integration.md** - SQLAlchemy setup, models, migrations, async patterns
- **project-structure.md** - Project organization, module structure, best practices
- **api-documentation.md** - OpenAPI customization, endpoint documentation, tags

Read these when you need detailed information about specific topics.

## Best Practices

1. **Use proper HTTP methods and status codes**
   - GET for retrieval, POST for creation, PUT/PATCH for updates, DELETE for deletion
   - Return 201 for creation, 204 for deletion, 404 for not found

2. **Always use response models**
   - Specify `response_model` for type safety and documentation
   - Use different schemas for create, update, and response

3. **Validate all input**
   - Use Pydantic models with Field constraints
   - Add custom validators when needed

4. **Structure your project properly**
   - Separate endpoints, schemas, models, and CRUD operations
   - Use dependency injection for database sessions

5. **Document your API**
   - Add docstrings to endpoints
   - Use descriptive parameter names and descriptions
   - Organize with tags

6. **Handle errors gracefully**
   - Use HTTPException with clear messages
   - Create custom exception classes
   - Document error responses

7. **Test your endpoints**
   - Write tests for all endpoints
   - Test success and error cases
   - Use TestClient for integration tests

8. **Version your API**
   - Include version in URL: `/api/v1/`
   - Plan for backward compatibility

9. **Keep endpoints focused**
   - One endpoint = one responsibility
   - Extract business logic to separate functions

10. **Use configuration management**
    - Store settings in environment variables
    - Use pydantic_settings for type-safe configuration

## Troubleshooting

**Import errors:**
- Ensure all directories have `__init__.py`
- Check Python path and package structure

**Validation errors:**
- Review Pydantic model definitions
- Check field types and constraints

**Database errors:**
- Verify DATABASE_URL in `.env`
- Run migrations if using Alembic
- Check database connection

**Documentation not showing:**
- Verify `docs_url` and `redoc_url` in FastAPI app
- Check that schemas have proper docstrings

## Learning Path

1. **Start simple**: Build a Hello World API
2. **Add structure**: Use Pydantic models for validation
3. **Implement CRUD**: Build complete CRUD endpoints
4. **Organize code**: Structure your project properly
5. **Add database**: Integrate SQLAlchemy for persistence
6. **Enhance docs**: Customize API documentation
7. **Add tests**: Write comprehensive tests
8. **Deploy**: Prepare for production

Follow this progression to build professional FastAPI applications!
