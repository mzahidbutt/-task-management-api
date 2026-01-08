"""
API Router

Aggregates all API endpoints for version 1.
"""

from fastapi import APIRouter
from app.api.v1.endpoints import items

api_router = APIRouter()

# Include endpoint routers here
api_router.include_router(items.router, prefix="/items", tags=["items"])

# Add more routers as needed:
# api_router.include_router(users.router, prefix="/users", tags=["users"])
