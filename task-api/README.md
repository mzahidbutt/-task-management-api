# Task Management API

A production-ready FastAPI application with SQLModel ORM and Neon PostgreSQL cloud database.

## Quick Start

### Prerequisites
- Python 3.12+
- uv package manager

### Installation

1. Install dependencies:
```bash
uv sync
```

2. Configure database:
```bash
# Copy .env.example to .env
# Add your Neon PostgreSQL connection string
DATABASE_URL=postgresql://user:pass@host/db?sslmode=require
```

3. Start the server:
```bash
uv run uvicorn main:app --reload
```

4. Open API documentation:
```
http://localhost:8000/docs
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API health check |
| GET | `/health/db` | Database connection check |
| POST | `/tasks` | Create a new task |
| GET | `/tasks` | List all tasks (with filters) |
| GET | `/tasks/{task_id}` | Get specific task |
| PUT | `/tasks/{task_id}` | Update a task |
| DELETE | `/tasks/{task_id}` | Delete a task |

## Testing

Run all tests:
```bash
uv run pytest tests/ -v
```

Run with coverage:
```bash
uv run pytest tests/ --cov=. --cov-report=term-missing
```

**Expected Results:**
- 36 tests passing
- 99% code coverage

## Tech Stack

- **FastAPI** (0.128.0+) - Modern web framework
- **SQLModel** (0.0.22+) - SQL databases with Python type hints
- **Neon PostgreSQL** - Serverless cloud database
- **pytest** (9.0.2+) - Testing framework
- **uv** - Fast Python package manager

## Project Structure

```
task-api/
├── main.py              # FastAPI application
├── .env                 # Environment variables (not in git)
├── .env.example         # Environment template
├── pyproject.toml       # Dependencies
├── uv.lock              # Locked dependencies
└── tests/               # Test suite
    ├── conftest.py      # Test configuration
    └── test_tasks.py    # API tests (36 tests)
```

## Features

- Complete CRUD operations
- Advanced filtering and pagination
- Cloud database integration
- Interactive API documentation
- Comprehensive test coverage (99%)
- Type-safe with Pydantic validation
- Health monitoring endpoints

## Development

Built as part of the Panaversity Q4 project demonstrating:
- Modern Python development practices
- Test-Driven Development (TDD)
- API design and documentation
- Cloud database integration
- Production-ready code quality

---

**For complete project documentation, see the [main README](../README.md)**
