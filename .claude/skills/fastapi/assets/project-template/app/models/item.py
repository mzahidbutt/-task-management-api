"""
Item Database Model

SQLAlchemy model for the items table.
"""

from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from sqlalchemy.sql import func
from app.db.database import Base


class Item(Base):
    """
    Item database model.

    Attributes:
        id: Primary key
        name: Item name (required)
        description: Item description (optional)
        price: Item price (required, must be positive)
        tax: Tax percentage (optional)
        is_active: Whether the item is active (default: True)
        created_at: Timestamp when item was created
        updated_at: Timestamp when item was last updated
    """

    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, index=True)
    description = Column(String(500), nullable=True)
    price = Column(Float, nullable=False)
    tax = Column(Float, nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return f"<Item(id={self.id}, name='{self.name}', price={self.price})>"
