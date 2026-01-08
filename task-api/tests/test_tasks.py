"""
Comprehensive tests for Task API endpoints.

Tests all CRUD operations:
- CREATE: POST /tasks
- READ: GET /tasks, GET /tasks/{id}
- UPDATE: PUT /tasks/{id}
- DELETE: DELETE /tasks/{id}
- Health checks: GET /, GET /health/db
"""

import pytest
from fastapi.testclient import TestClient


# ============================================================================
# CREATE TESTS - POST /tasks
# ============================================================================

def test_create_task_success(client: TestClient, sample_task_data: dict):
    """Test creating a task with valid data."""
    response = client.post("/tasks", json=sample_task_data)

    assert response.status_code == 201
    data = response.json()

    assert data["id"] is not None
    assert data["complain_no"] == sample_task_data["complain_no"]
    assert data["complain_remarks"] == sample_task_data["complain_remarks"]
    assert data["complain_status"] == sample_task_data["complain_status"]
    assert data["created_by"] == sample_task_data["created_by"]


def test_create_task_with_minimal_data(client: TestClient):
    """Test creating a task with only required fields."""
    minimal_data = {
        "complain_no": "MIN001",
        "created_by": "test_user"
    }

    response = client.post("/tasks", json=minimal_data)

    assert response.status_code == 201
    data = response.json()

    assert data["id"] is not None
    assert data["complain_no"] == "MIN001"
    assert data["complain_remarks"] is None
    assert data["complain_status"] == "pending"  # Default value
    assert data["created_by"] == "test_user"


def test_create_task_missing_required_field(client: TestClient):
    """Test creating a task without required field (complain_no)."""
    invalid_data = {
        "complain_remarks": "Missing complain_no",
        "created_by": "test_user"
    }

    response = client.post("/tasks", json=invalid_data)

    assert response.status_code == 422  # Validation error


def test_create_task_missing_created_by(client: TestClient):
    """Test creating a task without created_by field."""
    invalid_data = {
        "complain_no": "TEST002",
        "complain_remarks": "Missing created_by"
    }

    response = client.post("/tasks", json=invalid_data)

    assert response.status_code == 422  # Validation error


def test_create_multiple_tasks(client: TestClient):
    """Test creating multiple tasks."""
    task1_data = {
        "complain_no": "MULTI001",
        "complain_remarks": "First task",
        "created_by": "user1"
    }
    task2_data = {
        "complain_no": "MULTI002",
        "complain_remarks": "Second task",
        "created_by": "user2"
    }

    response1 = client.post("/tasks", json=task1_data)
    response2 = client.post("/tasks", json=task2_data)

    assert response1.status_code == 201
    assert response2.status_code == 201

    data1 = response1.json()
    data2 = response2.json()

    assert data1["id"] != data2["id"]  # Different IDs
    assert data1["complain_no"] == "MULTI001"
    assert data2["complain_no"] == "MULTI002"


# ============================================================================
# READ TESTS - GET /tasks (List all)
# ============================================================================

def test_list_tasks_empty(client: TestClient):
    """Test listing tasks when database is empty."""
    response = client.get("/tasks")

    assert response.status_code == 200
    assert response.json() == []


def test_list_tasks_with_data(client: TestClient, created_task: dict):
    """Test listing tasks when tasks exist."""
    response = client.get("/tasks")

    assert response.status_code == 200
    tasks = response.json()

    assert len(tasks) >= 1
    assert any(task["id"] == created_task["id"] for task in tasks)


def test_list_tasks_multiple(client: TestClient):
    """Test listing multiple tasks."""
    # Create 3 tasks
    for i in range(3):
        client.post("/tasks", json={
            "complain_no": f"LIST{i:03d}",
            "complain_remarks": f"Task {i}",
            "created_by": "test_user"
        })

    response = client.get("/tasks")

    assert response.status_code == 200
    tasks = response.json()

    assert len(tasks) >= 3


def test_filter_tasks_by_status(client: TestClient):
    """Test filtering tasks by status."""
    # Create tasks with different statuses
    client.post("/tasks", json={
        "complain_no": "STAT001",
        "complain_status": "pending",
        "created_by": "user1"
    })
    client.post("/tasks", json={
        "complain_no": "STAT002",
        "complain_status": "resolved",
        "created_by": "user1"
    })
    client.post("/tasks", json={
        "complain_no": "STAT003",
        "complain_status": "pending",
        "created_by": "user1"
    })

    # Filter by pending status
    response = client.get("/tasks?status=pending")

    assert response.status_code == 200
    tasks = response.json()

    assert len(tasks) >= 2
    assert all(task["complain_status"] == "pending" for task in tasks)


def test_filter_tasks_by_created_by(client: TestClient):
    """Test filtering tasks by creator."""
    # Create tasks by different users
    client.post("/tasks", json={
        "complain_no": "USER001",
        "created_by": "alice"
    })
    client.post("/tasks", json={
        "complain_no": "USER002",
        "created_by": "bob"
    })
    client.post("/tasks", json={
        "complain_no": "USER003",
        "created_by": "alice"
    })

    # Filter by alice
    response = client.get("/tasks?created_by=alice")

    assert response.status_code == 200
    tasks = response.json()

    assert len(tasks) >= 2
    assert all(task["created_by"] == "alice" for task in tasks)


def test_filter_tasks_by_status_and_created_by(client: TestClient):
    """Test filtering tasks by both status and creator."""
    # Create tasks with various combinations
    client.post("/tasks", json={
        "complain_no": "COMBO001",
        "complain_status": "pending",
        "created_by": "alice"
    })
    client.post("/tasks", json={
        "complain_no": "COMBO002",
        "complain_status": "resolved",
        "created_by": "alice"
    })
    client.post("/tasks", json={
        "complain_no": "COMBO003",
        "complain_status": "pending",
        "created_by": "bob"
    })

    # Filter by pending status AND alice
    response = client.get("/tasks?status=pending&created_by=alice")

    assert response.status_code == 200
    tasks = response.json()

    assert len(tasks) >= 1
    assert all(
        task["complain_status"] == "pending" and task["created_by"] == "alice"
        for task in tasks
    )


def test_list_tasks_pagination_skip(client: TestClient):
    """Test pagination with skip parameter."""
    # Create 5 tasks
    for i in range(5):
        client.post("/tasks", json={
            "complain_no": f"PAGE{i:03d}",
            "created_by": "test_user"
        })

    # Skip first 2 tasks
    response = client.get("/tasks?skip=2&limit=10")

    assert response.status_code == 200
    tasks = response.json()

    assert len(tasks) >= 3


def test_list_tasks_pagination_limit(client: TestClient):
    """Test pagination with limit parameter."""
    # Create 5 tasks
    for i in range(5):
        client.post("/tasks", json={
            "complain_no": f"LIM{i:03d}",
            "created_by": "test_user"
        })

    # Limit to 2 tasks
    response = client.get("/tasks?limit=2")

    assert response.status_code == 200
    tasks = response.json()

    assert len(tasks) <= 2


# ============================================================================
# READ TESTS - GET /tasks/{id} (Get single task)
# ============================================================================

def test_get_task_by_id_success(client: TestClient, created_task: dict):
    """Test getting a single task by ID."""
    task_id = created_task["id"]

    response = client.get(f"/tasks/{task_id}")

    assert response.status_code == 200
    data = response.json()

    assert data["id"] == task_id
    assert data["complain_no"] == created_task["complain_no"]
    assert data["created_by"] == created_task["created_by"]


def test_get_task_by_id_not_found(client: TestClient):
    """Test getting a non-existent task."""
    non_existent_id = 99999

    response = client.get(f"/tasks/{non_existent_id}")

    assert response.status_code == 404
    assert "not found" in response.json()["detail"].lower()


def test_get_task_by_id_invalid_id(client: TestClient):
    """Test getting a task with invalid ID format."""
    response = client.get("/tasks/invalid_id")

    assert response.status_code == 422  # Validation error


# ============================================================================
# UPDATE TESTS - PUT /tasks/{id}
# ============================================================================

def test_update_task_all_fields(client: TestClient, created_task: dict):
    """Test updating all fields of a task."""
    task_id = created_task["id"]
    update_data = {
        "complain_no": "UPDATED001",
        "complain_remarks": "Updated remarks",
        "complain_status": "resolved",
        "created_by": "updated_user"
    }

    response = client.put(f"/tasks/{task_id}", json=update_data)

    assert response.status_code == 200
    data = response.json()

    assert data["id"] == task_id
    assert data["complain_no"] == "UPDATED001"
    assert data["complain_remarks"] == "Updated remarks"
    assert data["complain_status"] == "resolved"
    assert data["created_by"] == "updated_user"


def test_update_task_partial_status_only(client: TestClient, created_task: dict):
    """Test updating only the status field."""
    task_id = created_task["id"]
    original_complain_no = created_task["complain_no"]

    update_data = {
        "complain_status": "in_progress"
    }

    response = client.put(f"/tasks/{task_id}", json=update_data)

    assert response.status_code == 200
    data = response.json()

    assert data["complain_status"] == "in_progress"
    assert data["complain_no"] == original_complain_no  # Unchanged


def test_update_task_partial_remarks_only(client: TestClient, created_task: dict):
    """Test updating only the remarks field."""
    task_id = created_task["id"]

    update_data = {
        "complain_remarks": "New remarks added"
    }

    response = client.put(f"/tasks/{task_id}", json=update_data)

    assert response.status_code == 200
    data = response.json()

    assert data["complain_remarks"] == "New remarks added"


def test_update_task_not_found(client: TestClient):
    """Test updating a non-existent task."""
    non_existent_id = 99999
    update_data = {
        "complain_status": "resolved"
    }

    response = client.put(f"/tasks/{non_existent_id}", json=update_data)

    assert response.status_code == 404
    assert "not found" in response.json()["detail"].lower()


def test_update_task_empty_body(client: TestClient, created_task: dict):
    """Test updating with empty request body."""
    task_id = created_task["id"]

    response = client.put(f"/tasks/{task_id}", json={})

    assert response.status_code == 200
    # Should return task unchanged


def test_update_task_clears_remarks(client: TestClient):
    """Test setting remarks to null."""
    # Create task with remarks
    create_response = client.post("/tasks", json={
        "complain_no": "CLEAR001",
        "complain_remarks": "Will be cleared",
        "created_by": "test_user"
    })
    task_id = create_response.json()["id"]

    # Update to clear remarks
    update_data = {
        "complain_remarks": None
    }

    response = client.put(f"/tasks/{task_id}", json=update_data)

    assert response.status_code == 200
    data = response.json()

    assert data["complain_remarks"] is None


# ============================================================================
# DELETE TESTS - DELETE /tasks/{id}
# ============================================================================

def test_delete_task_success(client: TestClient, created_task: dict):
    """Test deleting a task successfully."""
    task_id = created_task["id"]

    response = client.delete(f"/tasks/{task_id}")

    assert response.status_code == 200
    data = response.json()

    assert data["message"] == "Task deleted successfully"
    assert data["id"] == task_id

    # Verify task is actually deleted
    get_response = client.get(f"/tasks/{task_id}")
    assert get_response.status_code == 404


def test_delete_task_not_found(client: TestClient):
    """Test deleting a non-existent task."""
    non_existent_id = 99999

    response = client.delete(f"/tasks/{non_existent_id}")

    assert response.status_code == 404
    assert "not found" in response.json()["detail"].lower()


def test_delete_task_verify_removed_from_list(client: TestClient):
    """Test that deleted task doesn't appear in list."""
    # Create a task
    create_response = client.post("/tasks", json={
        "complain_no": "DEL001",
        "created_by": "test_user"
    })
    task_id = create_response.json()["id"]

    # Delete the task
    client.delete(f"/tasks/{task_id}")

    # List all tasks
    list_response = client.get("/tasks")
    tasks = list_response.json()

    # Verify deleted task is not in list
    assert not any(task["id"] == task_id for task in tasks)


def test_delete_task_twice(client: TestClient, created_task: dict):
    """Test deleting the same task twice."""
    task_id = created_task["id"]

    # First delete
    response1 = client.delete(f"/tasks/{task_id}")
    assert response1.status_code == 200

    # Second delete should fail
    response2 = client.delete(f"/tasks/{task_id}")
    assert response2.status_code == 404


# ============================================================================
# HEALTH CHECK TESTS
# ============================================================================

def test_health_check_root(client: TestClient):
    """Test the root health check endpoint."""
    response = client.get("/")

    assert response.status_code == 200
    data = response.json()

    assert data["status"] == "healthy"
    assert "message" in data
    assert "SQLModel" in data["message"]


def test_health_check_database(client: TestClient):
    """Test the database health check endpoint."""
    response = client.get("/health/db")

    assert response.status_code == 200
    data = response.json()

    assert data["status"] == "healthy"
    assert data["database"] == "connected"


# ============================================================================
# INTEGRATION TESTS (Multiple operations)
# ============================================================================

def test_full_crud_workflow(client: TestClient):
    """Test complete CRUD workflow: Create → Read → Update → Delete."""
    # 1. CREATE
    create_data = {
        "complain_no": "WORKFLOW001",
        "complain_remarks": "Initial remarks",
        "complain_status": "pending",
        "created_by": "workflow_user"
    }
    create_response = client.post("/tasks", json=create_data)
    assert create_response.status_code == 201
    task_id = create_response.json()["id"]

    # 2. READ (single)
    read_response = client.get(f"/tasks/{task_id}")
    assert read_response.status_code == 200
    assert read_response.json()["complain_no"] == "WORKFLOW001"

    # 3. UPDATE
    update_data = {"complain_status": "resolved"}
    update_response = client.put(f"/tasks/{task_id}", json=update_data)
    assert update_response.status_code == 200
    assert update_response.json()["complain_status"] == "resolved"

    # 4. DELETE
    delete_response = client.delete(f"/tasks/{task_id}")
    assert delete_response.status_code == 200

    # 5. VERIFY DELETED
    verify_response = client.get(f"/tasks/{task_id}")
    assert verify_response.status_code == 404


def test_create_and_filter_workflow(client: TestClient):
    """Test creating multiple tasks and filtering them."""
    # Create tasks with different attributes
    tasks_data = [
        {"complain_no": "FILTER001", "complain_status": "pending", "created_by": "alice"},
        {"complain_no": "FILTER002", "complain_status": "pending", "created_by": "bob"},
        {"complain_no": "FILTER003", "complain_status": "resolved", "created_by": "alice"},
    ]

    for task_data in tasks_data:
        response = client.post("/tasks", json=task_data)
        assert response.status_code == 201

    # Filter by pending status
    pending_response = client.get("/tasks?status=pending")
    pending_tasks = pending_response.json()
    assert len([t for t in pending_tasks if t["complain_status"] == "pending"]) >= 2

    # Filter by alice
    alice_response = client.get("/tasks?created_by=alice")
    alice_tasks = alice_response.json()
    assert len([t for t in alice_tasks if t["created_by"] == "alice"]) >= 2


def test_update_multiple_times(client: TestClient, created_task: dict):
    """Test updating the same task multiple times."""
    task_id = created_task["id"]

    # First update
    response1 = client.put(f"/tasks/{task_id}", json={"complain_status": "in_progress"})
    assert response1.status_code == 200
    assert response1.json()["complain_status"] == "in_progress"

    # Second update
    response2 = client.put(f"/tasks/{task_id}", json={"complain_status": "resolved"})
    assert response2.status_code == 200
    assert response2.json()["complain_status"] == "resolved"

    # Third update
    response3 = client.put(f"/tasks/{task_id}", json={"complain_remarks": "Final remarks"})
    assert response3.status_code == 200
    data = response3.json()
    assert data["complain_remarks"] == "Final remarks"
    assert data["complain_status"] == "resolved"  # Previous update persisted


# ============================================================================
# EDGE CASES AND ERROR HANDLING
# ============================================================================

def test_create_task_with_very_long_complain_no(client: TestClient):
    """Test creating a task with very long complain_no."""
    long_complain_no = "LONG" * 100  # 400 characters

    response = client.post("/tasks", json={
        "complain_no": long_complain_no,
        "created_by": "test_user"
    })

    assert response.status_code == 201
    assert response.json()["complain_no"] == long_complain_no


def test_create_task_with_special_characters(client: TestClient):
    """Test creating a task with special characters."""
    special_data = {
        "complain_no": "SPEC-001@#$",
        "complain_remarks": "Special chars: <>&\"'",
        "created_by": "user@example.com"
    }

    response = client.post("/tasks", json=special_data)

    assert response.status_code == 201
    data = response.json()
    assert data["complain_no"] == special_data["complain_no"]
    assert data["complain_remarks"] == special_data["complain_remarks"]


def test_list_tasks_with_invalid_query_params(client: TestClient):
    """Test listing tasks with invalid query parameters."""
    # Invalid skip value
    response1 = client.get("/tasks?skip=-1")
    # Should still work or return validation error

    # Invalid limit value
    response2 = client.get("/tasks?limit=-1")
    # Should still work or return validation error


def test_get_task_with_zero_id(client: TestClient):
    """Test getting a task with ID 0."""
    response = client.get("/tasks/0")

    assert response.status_code == 404


def test_create_task_with_empty_strings(client: TestClient):
    """Test creating a task with empty string values."""
    empty_data = {
        "complain_no": "",
        "complain_remarks": "",
        "created_by": ""
    }

    response = client.post("/tasks", json=empty_data)

    # Should accept empty strings (they're valid strings)
    assert response.status_code == 201
