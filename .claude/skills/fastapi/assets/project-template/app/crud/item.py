"""
Item CRUD Operations

Database operations for managing items using SQLAlchemy.
"""

from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.item import Item
from app.schemas.item import ItemCreate, ItemUpdate


def get_item(db: Session, item_id: int) -> Optional[Item]:
    """
    Get a single item by ID.

    Args:
        db: Database session
        item_id: ID of the item to retrieve

    Returns:
        Item if found, None otherwise
    """
    return db.query(Item).filter(Item.id == item_id).first()


def get_items(db: Session, skip: int = 0, limit: int = 100) -> List[Item]:
    """
    Get multiple items with pagination.

    Args:
        db: Database session
        skip: Number of items to skip (for pagination)
        limit: Maximum number of items to return

    Returns:
        List of items
    """
    return db.query(Item).offset(skip).limit(limit).all()


def get_active_items(db: Session, skip: int = 0, limit: int = 100) -> List[Item]:
    """
    Get only active items with pagination.

    Args:
        db: Database session
        skip: Number of items to skip (for pagination)
        limit: Maximum number of items to return

    Returns:
        List of active items
    """
    return db.query(Item).filter(Item.is_active == True).offset(skip).limit(limit).all()


def search_items(db: Session, search: str) -> List[Item]:
    """
    Search items by name.

    Args:
        db: Database session
        search: Search term to match against item names

    Returns:
        List of matching items
    """
    return db.query(Item).filter(Item.name.contains(search)).all()


def create_item(db: Session, item: ItemCreate) -> Item:
    """
    Create a new item in the database.

    Args:
        db: Database session
        item: Item data to create

    Returns:
        The created item with ID and timestamps
    """
    db_item = Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_item(db: Session, item_id: int, item: ItemUpdate) -> Optional[Item]:
    """
    Update an existing item.

    Args:
        db: Database session
        item_id: ID of the item to update
        item: Updated item data (only provided fields will be updated)

    Returns:
        Updated item if found, None otherwise
    """
    db_item = get_item(db, item_id)
    if not db_item:
        return None

    # Update only the fields that were provided
    update_data = item.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_item, field, value)

    db.commit()
    db.refresh(db_item)
    return db_item


def delete_item(db: Session, item_id: int) -> bool:
    """
    Delete an item from the database.

    Args:
        db: Database session
        item_id: ID of the item to delete

    Returns:
        True if item was deleted, False if item was not found
    """
    db_item = get_item(db, item_id)
    if not db_item:
        return False

    db.delete(db_item)
    db.commit()
    return True


def deactivate_item(db: Session, item_id: int) -> Optional[Item]:
    """
    Soft delete an item by marking it as inactive.

    Args:
        db: Database session
        item_id: ID of the item to deactivate

    Returns:
        Deactivated item if found, None otherwise
    """
    db_item = get_item(db, item_id)
    if not db_item:
        return None

    db_item.is_active = False
    db.commit()
    db.refresh(db_item)
    return db_item


def get_item_count(db: Session) -> int:
    """
    Get the total count of items in the database.

    Args:
        db: Database session

    Returns:
        Total number of items
    """
    return db.query(Item).count()


class CRUDItem:
    """
    CRUD operations class for items.

    This class provides a convenient interface for all CRUD operations.
    """

    def get(self, db: Session, item_id: int) -> Optional[Item]:
        return get_item(db, item_id)

    def get_multi(self, db: Session, skip: int = 0, limit: int = 100) -> List[Item]:
        return get_items(db, skip=skip, limit=limit)

    def create(self, db: Session, item: ItemCreate) -> Item:
        return create_item(db, item)

    def update(self, db: Session, item_id: int, item: ItemUpdate) -> Optional[Item]:
        return update_item(db, item_id, item)

    def delete(self, db: Session, item_id: int) -> bool:
        return delete_item(db, item_id)


crud_item = CRUDItem()
