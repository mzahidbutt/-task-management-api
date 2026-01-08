"""
Application Configuration

Manages environment variables and application settings using Pydantic.
"""

from typing import List
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""

    # API Configuration
    PROJECT_NAME: str = "FastAPI Project"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = "A professional FastAPI application"
    API_V1_STR: str = "/api/v1"

    # CORS Configuration
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:8000"]

    # Database Configuration
    DATABASE_URL: str = "sqlite:///./app.db"  # For SQLite (default)
    # DATABASE_URL: str = "postgresql://user:password@localhost/dbname"  # For PostgreSQL
    DB_ECHO: bool = False  # Set to True to log SQL queries

    # Security Configuration (uncomment when adding authentication)
    # SECRET_KEY: str = "your-secret-key-here-change-in-production"
    # ALGORITHM: str = "HS256"
    # ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
