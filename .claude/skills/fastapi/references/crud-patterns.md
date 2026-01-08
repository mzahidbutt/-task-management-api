# CRUD Patterns in FastAPI

This guide covers common CRUD (Create, Read, Update, Delete) patterns for building REST APIs with FastAPI.

## Table of Contents
- Basic CRUD Structure
- Response Models and Status Codes
- Pagination
- Filtering and Sorting
- Error Handling
- Validation Patterns

## Basic CRUD Structure

### Standard CRUD Endpoints

```python
from fastapi import APIRouter, HTTPException, status
from typing import List

router = APIRouter()

@router.get("/", response_model=List[ItemSchema])
async def list_items(skip: int = 0, limit: int = 100):
    """List all items with pagination"""
    return items[skip : skip + limit]

@router.get("/{item_id}", response_model=ItemSchema)
async def get_item(item_id: int):
    """Get a single item by ID"""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]

@router.post("/", response_model=ItemSchema, status_code=status.HTTP_201_CREATED)
async def create_item(item: ItemCreate):
    """Create a new item"""
    new_item = save_to_db(item)
    return new_item

@router.put("/{item_id}", response_model=ItemSchema)
async def update_item(item_id: int, item: ItemUpdate):
    """Update an existing item"""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    updated_item = update_in_db(item_id, item)
    return updated_item

@router.patch("/{item_id}", response_model=ItemSchema)
async def partial_update_item(item_id: int, item: ItemUpdate):
    """Partially update an item (only provided fields)"""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    update_data = item.model_dump(exclude_unset=True)
    updated_item = update_in_db(item_id, update_data)
    return updated_item

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: int):
    """Delete an item"""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    delete_from_db(item_id)
    return None
```

## Response Models and Status Codes

### Proper HTTP Status Codes

- `200 OK` - Successful GET, PUT, PATCH
- `201 Created` - Successful POST
- `204 No Content` - Successful DELETE
- `400 Bad Request` - Validation error
- `404 Not Found` - Resource doesn't exist
- `422 Unprocessable Entity` - Pydantic validation error (automatic)

### Multiple Response Models

```python
from typing import Union

@router.get("/{item_id}", response_model=Union[ItemPublic, ItemDetail])
async def get_item(item_id: int, detailed: bool = False):
    """Return different schemas based on query parameter"""
    item = get_from_db(item_id)
    if detailed:
        return ItemDetail.model_validate(item)
    return ItemPublic.model_validate(item)
```

## Pagination

### Offset-Based Pagination

```python
from typing import List
from pydantic import BaseModel

class PaginatedResponse(BaseModel):
    items: List[ItemSchema]
    total: int
    skip: int
    limit: int

@router.get("/", response_model=PaginatedResponse)
async def list_items(skip: int = 0, limit: int = 100):
    """Paginated list of items"""
    total = get_total_count()
    items = get_items(skip=skip, limit=limit)
    return {
        "items": items,
        "total": total,
        "skip": skip,
        "limit": limit,
    }
```

### Cursor-Based Pagination

```python
@router.get("/", response_model=List[ItemSchema])
async def list_items(cursor: int | None = None, limit: int = 100):
    """Cursor-based pagination for better performance"""
    items = get_items_after_cursor(cursor=cursor, limit=limit)
    return items
```

## Filtering and Sorting

### Query Parameters for Filtering

```python
@router.get("/", response_model=List[ItemSchema])
async def list_items(
    name: str | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
    in_stock: bool | None = None,
    skip: int = 0,
    limit: int = 100,
):
    """Filter items by multiple criteria"""
    filters = {
        "name": name,
        "min_price": min_price,
        "max_price": max_price,
        "in_stock": in_stock,
    }
    # Remove None values
    filters = {k: v for k, v in filters.items() if v is not None}

    items = get_filtered_items(filters, skip=skip, limit=limit)
    return items
```

### Sorting

```python
from enum import Enum

class SortOrder(str, Enum):
    asc = "asc"
    desc = "desc"

class ItemSortField(str, Enum):
    name = "name"
    price = "price"
    created_at = "created_at"

@router.get("/", response_model=List[ItemSchema])
async def list_items(
    sort_by: ItemSortField = ItemSortField.created_at,
    sort_order: SortOrder = SortOrder.desc,
    skip: int = 0,
    limit: int = 100,
):
    """Sort items by specified field"""
    items = get_sorted_items(
        sort_by=sort_by,
        sort_order=sort_order,
        skip=skip,
        limit=limit,
    )
    return items
```

## Error Handling

### Custom Exception Classes

```python
class ItemNotFoundError(HTTPException):
    def __init__(self, item_id: int):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found",
        )

class DuplicateItemError(HTTPException):
    def __init__(self, name: str):
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Item with name '{name}' already exists",
        )

# Usage
@router.get("/{item_id}")
async def get_item(item_id: int):
    item = get_from_db(item_id)
    if not item:
        raise ItemNotFoundError(item_id)
    return item
```

### Global Exception Handlers

```python
from fastapi import Request
from fastapi.responses import JSONResponse

@app.exception_handler(ItemNotFoundError)
async def item_not_found_handler(request: Request, exc: ItemNotFoundError):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": "item_not_found", "detail": exc.detail},
    )
```

## Validation Patterns

### Custom Validators

```python
from pydantic import BaseModel, field_validator, model_validator

class ItemCreate(BaseModel):
    name: str
    price: float
    discount: float | None = None

    @field_validator("name")
    @classmethod
    def name_must_not_be_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Name cannot be empty or whitespace")
        return v.strip()

    @field_validator("price")
    @classmethod
    def price_must_be_positive(cls, v: float) -> float:
        if v <= 0:
            raise ValueError("Price must be positive")
        return v

    @model_validator(mode="after")
    def check_discount(self):
        if self.discount and self.discount >= self.price:
            raise ValueError("Discount cannot be greater than or equal to price")
        return self
```

### Field Constraints

```python
from pydantic import BaseModel, Field

class ItemCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: str | None = Field(None, max_length=500)
    price: float = Field(..., gt=0, le=1000000)
    quantity: int = Field(..., ge=0)
    tags: list[str] = Field(default_factory=list, max_length=10)
```

## Bulk Operations

### Bulk Create

```python
@router.post("/bulk", response_model=List[ItemSchema], status_code=201)
async def create_items_bulk(items: List[ItemCreate]):
    """Create multiple items at once"""
    created_items = []
    for item in items:
        created_item = save_to_db(item)
        created_items.append(created_item)
    return created_items
```

### Bulk Update

```python
class BulkUpdateRequest(BaseModel):
    ids: List[int]
    update_data: ItemUpdate

@router.patch("/bulk", response_model=List[ItemSchema])
async def update_items_bulk(request: BulkUpdateRequest):
    """Update multiple items with same data"""
    updated_items = []
    for item_id in request.ids:
        updated_item = update_in_db(item_id, request.update_data)
        updated_items.append(updated_item)
    return updated_items
```

### Bulk Delete

```python
class BulkDeleteRequest(BaseModel):
    ids: List[int]

@router.delete("/bulk", status_code=204)
async def delete_items_bulk(request: BulkDeleteRequest):
    """Delete multiple items"""
    for item_id in request.ids:
        delete_from_db(item_id)
    return None
```

## Best Practices

1. **Use appropriate HTTP methods**: GET for retrieval, POST for creation, PUT for full updates, PATCH for partial updates, DELETE for deletion
2. **Return proper status codes**: 201 for creation, 204 for deletion, 404 for not found
3. **Use response models**: Always specify `response_model` for type safety and documentation
4. **Implement pagination**: Don't return all records at once
5. **Add filtering and sorting**: Make your API flexible
6. **Handle errors gracefully**: Use HTTPException with clear messages
7. **Validate input**: Use Pydantic models with validators
8. **Use appropriate schemas**: Different schemas for create, update, and response
9. **Document your endpoints**: Add docstrings for automatic OpenAPI docs
10. **Keep endpoints focused**: One endpoint = one responsibility
