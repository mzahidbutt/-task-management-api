"""
Tests for Items Endpoints

Example test file showing how to test FastAPI endpoints.
To run: pip install pytest httpx, then: pytest
"""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_root():
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_health_check():
    """Test health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_create_item():
    """Test creating a new item"""
    response = client.post(
        "/api/v1/items/",
        json={"name": "Test Item", "description": "A test item", "price": 10.99, "tax": 5.5},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test Item"
    assert data["price"] == 10.99
    assert "id" in data


def test_read_items():
    """Test listing items"""
    # First create an item
    client.post(
        "/api/v1/items/",
        json={"name": "Item 1", "price": 5.99},
    )

    # Then retrieve items
    response = client.get("/api/v1/items/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_read_item():
    """Test retrieving a specific item"""
    # Create an item
    create_response = client.post(
        "/api/v1/items/",
        json={"name": "Item 2", "price": 15.99},
    )
    item_id = create_response.json()["id"]

    # Retrieve the item
    response = client.get(f"/api/v1/items/{item_id}")
    assert response.status_code == 200
    assert response.json()["id"] == item_id


def test_read_item_not_found():
    """Test retrieving a non-existent item"""
    response = client.get("/api/v1/items/99999")
    assert response.status_code == 404


def test_update_item():
    """Test updating an item"""
    # Create an item
    create_response = client.post(
        "/api/v1/items/",
        json={"name": "Item 3", "price": 20.99},
    )
    item_id = create_response.json()["id"]

    # Update the item
    response = client.put(
        f"/api/v1/items/{item_id}",
        json={"name": "Updated Item", "price": 25.99},
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Item"
    assert response.json()["price"] == 25.99


def test_delete_item():
    """Test deleting an item"""
    # Create an item
    create_response = client.post(
        "/api/v1/items/",
        json={"name": "Item 4", "price": 30.99},
    )
    item_id = create_response.json()["id"]

    # Delete the item
    response = client.delete(f"/api/v1/items/{item_id}")
    assert response.status_code == 204

    # Verify it's deleted
    get_response = client.get(f"/api/v1/items/{item_id}")
    assert get_response.status_code == 404
