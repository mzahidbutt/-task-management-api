# API Documentation and Best Practices

This guide covers customizing FastAPI's automatic documentation and following API best practices.

## Table of Contents
- OpenAPI Customization
- Endpoint Documentation
- Response Models
- Tags and Groups
- Security Documentation
- Best Practices

## OpenAPI Customization

### Basic Application Metadata

```python
from fastapi import FastAPI

app = FastAPI(
    title="My API",
    description="A comprehensive API for managing items",
    version="1.0.0",
    terms_of_service="https://example.com/terms/",
    contact={
        "name": "API Support",
        "url": "https://example.com/contact/",
        "email": "support@example.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
)
```

### Custom OpenAPI URL

```python
app = FastAPI(
    title="My API",
    # Customize OpenAPI schema URL
    openapi_url="/api/v1/openapi.json",
    # Customize Swagger UI URL
    docs_url="/api/v1/docs",
    # Customize ReDoc URL
    redoc_url="/api/v1/redoc",
)
```

### Disable Documentation in Production

```python
from app.core.config import settings

app = FastAPI(
    title="My API",
    docs_url="/docs" if settings.ENVIRONMENT == "development" else None,
    redoc_url="/redoc" if settings.ENVIRONMENT == "development" else None,
)
```

### Custom OpenAPI Schema

```python
from fastapi.openapi.utils import get_openapi

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="Custom API",
        version="2.0.0",
        description="Custom OpenAPI schema",
        routes=app.routes,
    )

    # Add custom fields
    openapi_schema["info"]["x-logo"] = {
        "url": "https://example.com/logo.png"
    }

    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
```

## Endpoint Documentation

### Docstrings and Descriptions

```python
@router.post("/", response_model=Item, status_code=201)
async def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    """
    Create a new item with all the information.

    This endpoint allows you to create a new item in the system.
    The item must have a unique name.

    - **name**: The name of the item (required, max 100 characters)
    - **description**: Optional description of the item (max 500 characters)
    - **price**: The price of the item (required, must be positive)
    - **tax**: Optional tax percentage (0-100)

    Returns the created item with its assigned ID.
    """
    return crud_item.create(db, obj_in=item)
```

### Parameter Documentation

```python
from fastapi import Path, Query

@router.get("/{item_id}")
async def read_item(
    item_id: int = Path(..., title="Item ID", description="The ID of the item to retrieve", ge=1),
    q: str | None = Query(None, title="Search query", description="Optional search term", max_length=50),
    skip: int = Query(0, title="Skip", description="Number of items to skip", ge=0),
    limit: int = Query(100, title="Limit", description="Maximum number of items to return", ge=1, le=100),
):
    """Retrieve an item by ID with optional filtering"""
    pass
```

### Response Documentation

```python
from fastapi import status
from typing import Dict, Any

@router.get(
    "/{item_id}",
    response_model=Item,
    responses={
        200: {
            "description": "Item found successfully",
            "content": {
                "application/json": {
                    "example": {"id": 1, "name": "Item", "price": 10.99}
                }
            },
        },
        404: {
            "description": "Item not found",
            "content": {
                "application/json": {
                    "example": {"detail": "Item with id 1 not found"}
                }
            },
        },
    },
)
async def read_item(item_id: int):
    """Get an item by ID"""
    pass
```

### Multiple Response Models

```python
from typing import Union
from pydantic import BaseModel

class ErrorResponse(BaseModel):
    error: str
    detail: str

class SuccessResponse(BaseModel):
    message: str
    data: Dict[str, Any]

@router.post(
    "/process",
    responses={
        200: {"model": SuccessResponse},
        400: {"model": ErrorResponse},
        500: {"model": ErrorResponse},
    },
)
async def process_data(data: Dict[str, Any]):
    """Process data with different response types"""
    pass
```

## Tags and Groups

### Organizing Endpoints with Tags

```python
from fastapi import FastAPI, APIRouter

app = FastAPI()

items_router = APIRouter(prefix="/items", tags=["items"])
users_router = APIRouter(prefix="/users", tags=["users"])

@items_router.get("/")
async def read_items():
    """All items endpoints are grouped under 'items' tag"""
    pass

@users_router.get("/")
async def read_users():
    """All users endpoints are grouped under 'users' tag"""
    pass

app.include_router(items_router)
app.include_router(users_router)
```

### Tag Metadata

```python
from fastapi import FastAPI

tags_metadata = [
    {
        "name": "items",
        "description": "Operations with items. Manage inventory and product catalog.",
    },
    {
        "name": "users",
        "description": "User management and authentication operations.",
        "externalDocs": {
            "description": "User documentation",
            "url": "https://example.com/docs/users",
        },
    },
    {
        "name": "orders",
        "description": "Order processing and management.",
    },
]

app = FastAPI(openapi_tags=tags_metadata)

@app.get("/items/", tags=["items"])
async def read_items():
    pass

@app.get("/users/", tags=["users"])
async def read_users():
    pass
```

### Multiple Tags

```python
@router.get("/special-items", tags=["items", "special", "featured"])
async def read_special_items():
    """This endpoint appears under multiple tags"""
    pass
```

## Security Documentation

### OAuth2 Documentation

```python
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    OAuth2 compatible token login.

    Get an access token for future requests.
    """
    return {"access_token": "token", "token_type": "bearer"}

@app.get("/users/me")
async def read_users_me(token: str = Depends(oauth2_scheme)):
    """
    Get current user.

    Requires authentication with Bearer token.
    """
    return {"user": "current user"}
```

### API Key Documentation

```python
from fastapi import Security, FastAPI
from fastapi.security import APIKeyHeader

api_key_header = APIKeyHeader(name="X-API-Key")

app = FastAPI()

@app.get("/protected")
async def protected_route(api_key: str = Security(api_key_header)):
    """
    Protected endpoint requiring API key.

    Provide your API key in the X-API-Key header.
    """
    return {"message": "Access granted"}
```

## Response Models

### Different Response Models

```python
from pydantic import BaseModel

class ItemPublic(BaseModel):
    """Public view of an item"""
    id: int
    name: str
    price: float

class ItemDetail(BaseModel):
    """Detailed view including internal data"""
    id: int
    name: str
    description: str | None
    price: float
    cost: float
    margin: float
    supplier_id: int

@router.get("/{item_id}/public", response_model=ItemPublic)
async def get_item_public(item_id: int):
    """Get public item information"""
    pass

@router.get("/{item_id}/detail", response_model=ItemDetail)
async def get_item_detail(item_id: int):
    """Get detailed item information (admin only)"""
    pass
```

### Exclude Fields from Response

```python
class User(BaseModel):
    username: str
    email: str
    full_name: str | None = None
    password: str  # We don't want to return this

class UserPublic(BaseModel):
    username: str
    email: str
    full_name: str | None = None

@router.post("/users/", response_model=UserPublic)
async def create_user(user: User):
    """Create user - password is excluded from response"""
    return user
```

### Response Model with Examples

```python
from pydantic import BaseModel, Field

class Item(BaseModel):
    name: str = Field(..., example="Widget")
    description: str | None = Field(None, example="A useful widget")
    price: float = Field(..., example=29.99)
    tax: float | None = Field(None, example=2.40)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Premium Widget",
                    "description": "The best widget available",
                    "price": 49.99,
                    "tax": 4.00
                }
            ]
        }
    }
```

## Best Practices

### 1. Consistent Naming

Use consistent naming conventions:
```python
# Good - plural for collections, singular for items
@router.get("/items/")          # List items
@router.get("/items/{item_id}") # Get single item
@router.post("/items/")         # Create item

# Avoid inconsistent naming
@router.get("/item_list/")      # Bad
@router.get("/getItem/{id}")    # Bad
```

### 2. Use Proper HTTP Methods

```python
@router.get("/items/")         # Retrieve (safe, idempotent)
@router.post("/items/")        # Create (not idempotent)
@router.put("/items/{id}")     # Full update (idempotent)
@router.patch("/items/{id}")   # Partial update (not idempotent)
@router.delete("/items/{id}")  # Delete (idempotent)
```

### 3. Return Appropriate Status Codes

```python
from fastapi import status

@router.post("/", status_code=status.HTTP_201_CREATED)  # Created
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)  # No content
@router.get("/", status_code=status.HTTP_200_OK)  # OK (default)
```

### 4. Use Response Models

Always specify response models for documentation:
```python
# Good
@router.get("/", response_model=List[Item])
async def read_items():
    return items

# Avoid
@router.get("/")
async def read_items():
    return items  # Response structure is unclear
```

### 5. Provide Examples

```python
from pydantic import Field

class Item(BaseModel):
    name: str = Field(..., example="Widget")
    price: float = Field(..., gt=0, example=29.99)
```

### 6. Version Your API

```python
# Include version in URL
app.include_router(api_router, prefix="/api/v1")

# Or in headers
@router.get("/items/")
async def read_items(api_version: str = Header("1.0")):
    pass
```

### 7. Document Errors

```python
@router.get(
    "/{item_id}",
    responses={
        404: {"description": "Item not found"},
        400: {"description": "Invalid item ID"},
    },
)
async def read_item(item_id: int):
    pass
```

### 8. Use Enums for Fixed Values

```python
from enum import Enum

class ItemType(str, Enum):
    electronics = "electronics"
    clothing = "clothing"
    food = "food"

@router.get("/items/")
async def read_items(item_type: ItemType | None = None):
    """Filter items by type - shows dropdown in docs"""
    pass
```

### 9. Deprecate Endpoints Properly

```python
@router.get("/old-endpoint", deprecated=True)
async def old_endpoint():
    """
    This endpoint is deprecated.

    Use `/new-endpoint` instead.
    """
    pass
```

### 10. Keep Endpoints Focused

```python
# Good - Single responsibility
@router.get("/items/{item_id}")
async def get_item(item_id: int):
    """Get a single item"""
    pass

@router.get("/items/{item_id}/reviews")
async def get_item_reviews(item_id: int):
    """Get reviews for an item"""
    pass

# Avoid - Too many responsibilities
@router.get("/items/{item_id}")
async def get_item(
    item_id: int,
    include_reviews: bool = False,
    include_related: bool = False,
    include_history: bool = False,
):
    """Gets too complex"""
    pass
```

## Documentation URLs

After running your FastAPI app, access documentation at:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI Schema**: http://localhost:8000/openapi.json

These are interactive and automatically updated!
