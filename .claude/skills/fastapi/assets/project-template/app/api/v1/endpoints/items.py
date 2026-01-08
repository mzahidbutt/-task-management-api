"""
Items Endpoints

CRUD endpoints for managing items with SQLAlchemy database integration.
"""

from typing import List
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.item import Item, ItemCreate, ItemUpdate
from app.crud.item import (
    get_item,
    get_items,
    get_active_items,
    create_item,
    update_item,
    delete_item,
    deactivate_item,
    search_items,
    get_item_count,
)

router = APIRouter()


@router.get("/", response_model=List[Item])
def read_items(
    skip: int = Query(0, ge=0, description="Number of items to skip"),
    limit: int = Query(100, ge=1, le=1000, description="Maximum number of items to return"),
    active_only: bool = Query(False, description="Return only active items"),
    db: Session = Depends(get_db),
):
    """
    Retrieve all items with pagination.

    - **skip**: Number of items to skip (for pagination)
    - **limit**: Maximum number of items to return (1-1000)
    - **active_only**: If True, return only active items
    """
    if active_only:
        items = get_active_items(db, skip=skip, limit=limit)
    else:
        items = get_items(db, skip=skip, limit=limit)
    return items


@router.get("/search/", response_model=List[Item])
def search_items_endpoint(
    q: str = Query(..., min_length=1, description="Search query"),
    db: Session = Depends(get_db),
):
    """
    Search items by name.

    - **q**: Search term to match against item names
    """
    items = search_items(db, search=q)
    return items


@router.get("/count/")
def count_items(db: Session = Depends(get_db)):
    """
    Get the total count of items in the database.
    """
    count = get_item_count(db)
    return {"count": count}


@router.get("/{item_id}", response_model=Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a specific item by ID.

    - **item_id**: The ID of the item to retrieve
    """
    db_item = get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found",
        )
    return db_item


@router.post("/", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_new_item(item: ItemCreate, db: Session = Depends(get_db)):
    """
    Create a new item.

    - **name**: Item name (required, 1-100 characters)
    - **description**: Item description (optional, max 500 characters)
    - **price**: Item price (required, must be positive)
    - **tax**: Tax percentage (optional, 0-100)
    """
    db_item = create_item(db=db, item=item)
    return db_item


@router.put("/{item_id}", response_model=Item)
def update_existing_item(
    item_id: int,
    item: ItemUpdate,
    db: Session = Depends(get_db),
):
    """
    Update an existing item (full update).

    - **item_id**: The ID of the item to update
    - Provide all fields you want to update
    """
    db_item = update_item(db, item_id=item_id, item=item)
    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found",
        )
    return db_item


@router.patch("/{item_id}", response_model=Item)
def partial_update_item(
    item_id: int,
    item: ItemUpdate,
    db: Session = Depends(get_db),
):
    """
    Partially update an item (only provided fields will be updated).

    - **item_id**: The ID of the item to update
    - Provide only the fields you want to update
    """
    db_item = update_item(db, item_id=item_id, item=item)
    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found",
        )
    return db_item


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_existing_item(item_id: int, db: Session = Depends(get_db)):
    """
    Delete an item (hard delete - permanently removes from database).

    - **item_id**: The ID of the item to delete
    """
    success = delete_item(db, item_id=item_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found",
        )
    return None


@router.post("/{item_id}/deactivate", response_model=Item)
def deactivate_existing_item(item_id: int, db: Session = Depends(get_db)):
    """
    Deactivate an item (soft delete - marks as inactive but keeps in database).

    - **item_id**: The ID of the item to deactivate
    """
    db_item = deactivate_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found",
        )
    return db_item
