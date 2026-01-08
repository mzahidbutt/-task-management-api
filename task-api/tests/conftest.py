"""
Pytest configuration and fixtures for testing the Task API.
"""

import pytest
from sqlmodel import SQLModel, create_engine, Session
from fastapi.testclient import TestClient
from typing import Generator

from main import app, get_session, Task

# Use in-memory SQLite database for testing
TEST_DATABASE_URL = "sqlite:///./test.db"

@pytest.fixture(name="engine")
def engine_fixture():
    """Create a test database engine."""
    engine = create_engine(
        TEST_DATABASE_URL,
        connect_args={"check_same_thread": False},
        echo=False
    )
    SQLModel.metadata.create_all(engine)
    yield engine
    SQLModel.metadata.drop_all(engine)


@pytest.fixture(name="session")
def session_fixture(engine) -> Generator[Session, None, None]:
    """Create a test database session."""
    with Session(engine) as session:
        yield session


@pytest.fixture(name="client")
def client_fixture(session: Session) -> Generator[TestClient, None, None]:
    """Create a test client with database session override."""

    def get_session_override():
        return session

    app.dependency_overrides[get_session] = get_session_override

    with TestClient(app) as client:
        yield client

    app.dependency_overrides.clear()


@pytest.fixture(name="sample_task_data")
def sample_task_data_fixture():
    """Sample task data for testing."""
    return {
        "complain_no": "TEST001",
        "complain_remarks": "Test complaint",
        "complain_status": "pending",
        "created_by": "test_user"
    }


@pytest.fixture(name="created_task")
def created_task_fixture(client: TestClient, sample_task_data: dict):
    """Create a task and return its data."""
    response = client.post("/tasks", json=sample_task_data)
    return response.json()
