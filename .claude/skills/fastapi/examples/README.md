# FastAPI CRUD + Database Integration Examples

This directory contains complete, standalone examples demonstrating FastAPI with SQLAlchemy database integration.

## Complete CRUD Example

The `crud_database_example.py` file is a single-file FastAPI application that demonstrates:

- **Database Setup**: SQLAlchemy configuration with SQLite
- **Database Models**: SQLAlchemy ORM models
- **Pydantic Schemas**: Request/response validation
- **CRUD Operations**: Complete Create, Read, Update, Delete functions
- **FastAPI Endpoints**: RESTful API endpoints with database integration
- **Error Handling**: Proper HTTP status codes and error responses
- **API Documentation**: Auto-generated OpenAPI/Swagger docs

### Running the Example

1. **Install dependencies**:
   ```bash
   pip install fastapi uvicorn sqlalchemy
   ```

2. **Run the application**:
   ```bash
   python crud_database_example.py
   ```

3. **Access the API**:
   - API Documentation: http://localhost:8000/docs
   - Alternative Docs: http://localhost:8000/redoc
   - API Root: http://localhost:8000

### Testing the API

#### Create an Item
```bash
curl -X POST "http://localhost:8000/items/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Laptop",
    "description": "Gaming laptop",
    "price": 1299.99,
    "tax": 10.5
  }'
```

#### Get All Items
```bash
curl http://localhost:8000/items/
```

#### Get Specific Item
```bash
curl http://localhost:8000/items/1
```

#### Search Items
```bash
curl "http://localhost:8000/items/search/?q=Laptop"
```

#### Update Item
```bash
curl -X PUT "http://localhost:8000/items/1" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Gaming Laptop",
    "price": 1199.99
  }'
```

#### Partial Update
```bash
curl -X PATCH "http://localhost:8000/items/1" \
  -H "Content-Type: application/json" \
  -d '{
    "price": 999.99
  }'
```

#### Deactivate Item (Soft Delete)
```bash
curl -X POST "http://localhost:8000/items/1/deactivate"
```

#### Delete Item (Hard Delete)
```bash
curl -X DELETE "http://localhost:8000/items/1"
```

### Features Demonstrated

1. **Database Integration**
   - SQLAlchemy ORM setup
   - Database session management
   - Automatic table creation

2. **CRUD Operations**
   - Create: POST /items/
   - Read: GET /items/ and GET /items/{id}
   - Update: PUT /items/{id} and PATCH /items/{id}
   - Delete: DELETE /items/{id}

3. **Advanced Features**
   - Pagination (skip/limit parameters)
   - Filtering (active_only parameter)
   - Search functionality
   - Soft delete (deactivate)
   - Timestamps (created_at, updated_at)

4. **Best Practices**
   - Proper HTTP status codes
   - Error handling with HTTPException
   - Pydantic validation
   - Response models
   - API documentation
   - Dependency injection

### Database

The example uses SQLite (`items_example.db`) which will be created automatically when you run the application. No additional setup required!

For production, you can easily switch to PostgreSQL, MySQL, or other databases supported by SQLAlchemy by changing the `DATABASE_URL`.

### Next Steps

After running this example:
1. Try all the endpoints using the interactive docs at `/docs`
2. Modify the Item model to add new fields
3. Add new endpoints for specific use cases
4. Switch to PostgreSQL for production
5. Add authentication and authorization
6. Implement database migrations with Alembic
