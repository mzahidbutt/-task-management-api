"""
Database Configuration and Session Management

This module sets up SQLAlchemy for database operations.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Create database engine
# For SQLite, we need to use check_same_thread=False to allow FastAPI to use the same connection across threads
engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in settings.DATABASE_URL else {},
    echo=settings.DB_ECHO,  # Set to True to log all SQL queries
)

# Create session factory
# autocommit=False: Transactions need to be explicitly committed
# autoflush=False: Changes are not automatically flushed to the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all database models
Base = declarative_base()


def get_db():
    """
    Database session dependency for FastAPI endpoints.

    Yields a database session and ensures it's closed after use.

    Usage:
        @app.get("/items")
        def read_items(db: Session = Depends(get_db)):
            return db.query(Item).all()
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_tables():
    """
    Create all tables in the database.

    This should be called once when initializing the database.
    In production, use Alembic migrations instead.
    """
    Base.metadata.create_all(bind=engine)


def drop_tables():
    """
    Drop all tables from the database.

    WARNING: This will delete all data!
    Only use in development/testing.
    """
    Base.metadata.drop_all(bind=engine)
