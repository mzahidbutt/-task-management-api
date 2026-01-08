"""
Item Schemas

Pydantic models for request/response validation.
"""

from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict


class ItemBase(BaseModel):
    """Base schema with common item attributes"""

    name: str = Field(..., min_length=1, max_length=100, description="Item name")
    description: str | None = Field(None, max_length=500, description="Item description")
    price: float = Field(..., gt=0, description="Item price (must be positive)")
    tax: float | None = Field(None, ge=0, le=100, description="Tax percentage (0-100)")


class ItemCreate(ItemBase):
    """Schema for creating a new item (no ID required)"""

    pass


class ItemUpdate(BaseModel):
    """Schema for updating an item (all fields optional)"""

    name: str | None = Field(None, min_length=1, max_length=100)
    description: str | None = Field(None, max_length=500)
    price: float | None = Field(None, gt=0)
    tax: float | None = Field(None, ge=0, le=100)


class Item(ItemBase):
    """Schema for item response (includes ID and metadata)"""

    id: int = Field(..., description="Item ID")
    is_active: bool = Field(default=True, description="Whether the item is active")
    created_at: datetime = Field(..., description="When the item was created")
    updated_at: datetime | None = Field(None, description="When the item was last updated")

    model_config = ConfigDict(from_attributes=True)  # Enables ORM mode for database models
