# FastAPI Project Template

A professional FastAPI project structure with SQLAlchemy database integration and CRUD operations.

## Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment:**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

3. **Run the application:**
   ```bash
   # Development mode (auto-reload)
   fastapi dev main.py

   # Production mode
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

4. **Access the API:**
   - API: http://localhost:8000
   - Interactive docs: http://localhost:8000/docs
   - Alternative docs: http://localhost:8000/redoc

## Project Structure

```
.
├── main.py                 # Application entry point
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── api.py      # API router aggregator
│   │       └── endpoints/  # Individual endpoint modules
│   ├── core/
│   │   └── config.py       # Configuration management
│   ├── crud/               # Database operations
│   │   └── item.py         # Item CRUD operations
│   ├── db/                 # Database setup
│   │   └── database.py     # SQLAlchemy configuration
│   ├── models/             # SQLAlchemy ORM models
│   │   └── item.py         # Item database model
│   └── schemas/            # Pydantic models for validation
│       └── item.py         # Item request/response schemas
├── tests/                  # Test files
├── requirements.txt        # Project dependencies
└── .env                    # Environment variables (create from .env.example)
```

## Features

This template includes:

- **SQLAlchemy Database Integration** - Complete database setup with SQLite (easily switchable to PostgreSQL)
- **CRUD Operations** - Full Create, Read, Update, Delete functionality
- **Pydantic Validation** - Request/response validation with type hints
- **Auto-generated API Documentation** - Swagger UI and ReDoc
- **Professional Project Structure** - Organized, maintainable code
- **Dependency Injection** - Database session management
- **Timestamps** - Automatic created_at and updated_at tracking
- **Soft Delete** - Deactivate items without removing from database

## API Endpoints

The template includes a complete CRUD API for items with database persistence:

**Basic CRUD:**
- `GET /api/v1/items/` - List all items (with pagination)
- `GET /api/v1/items/{item_id}` - Get specific item
- `POST /api/v1/items/` - Create new item
- `PUT /api/v1/items/{item_id}` - Update item (full update)
- `PATCH /api/v1/items/{item_id}` - Partial update item
- `DELETE /api/v1/items/{item_id}` - Delete item (hard delete)

**Advanced Features:**
- `GET /api/v1/items/search/?q=query` - Search items by name
- `GET /api/v1/items/count/` - Get total count of items
- `POST /api/v1/items/{item_id}/deactivate` - Deactivate item (soft delete)
- Query parameters: `skip`, `limit`, `active_only` for pagination and filtering

## Database

The template uses SQLite by default (configured in `.env`), which creates a file `app.db` in the project root. The database tables are created automatically on application startup.

To switch to PostgreSQL:
1. Install PostgreSQL driver: `pip install psycopg2-binary`
2. Update `DATABASE_URL` in `.env`:
   ```
   DATABASE_URL=postgresql://user:password@localhost/dbname
   ```

## Adding New Endpoints

1. Create a database model in `app/models/`
2. Create Pydantic schemas in `app/schemas/`
3. Create CRUD operations in `app/crud/`
4. Create endpoint file in `app/api/v1/endpoints/`
5. Register the router in `app/api/v1/api.py`

## Testing the API

Try creating an item:
```bash
curl -X POST "http://localhost:8000/api/v1/items/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Laptop",
    "description": "Gaming laptop",
    "price": 1299.99,
    "tax": 10.5
  }'
```

## Next Steps

- Add more models and endpoints
- Implement authentication (JWT tokens)
- Add database migrations with Alembic
- Write tests with pytest
- Add logging and monitoring
- Configure deployment (Docker, cloud platforms)
