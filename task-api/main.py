from fastapi import FastAPI, HTTPException, Depends
from sqlmodel import SQLModel, Field, create_engine, Session, select
from typing import Optional
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Database configuration
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set in .env file")

# SQLModel setup
engine = create_engine(DATABASE_URL, echo=True)

# Create tables
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Database Model - This is both a SQLModel table and Pydantic model
class Task(SQLModel, table=True):
    __tablename__ = "tasks"

    id: Optional[int] = Field(default=None, primary_key=True)
    complain_no: str = Field(index=True)
    complain_remarks: Optional[str] = Field(default=None)
    complain_status: str = Field(default="pending")
    created_by: str

# Pydantic Models for API
class TaskCreate(SQLModel):
    complain_no: str
    complain_remarks: Optional[str] = None
    complain_status: str = "pending"
    created_by: str

class TaskUpdate(SQLModel):
    complain_no: Optional[str] = None
    complain_remarks: Optional[str] = None
    complain_status: Optional[str] = None
    created_by: Optional[str] = None

class TaskResponse(SQLModel):
    id: int
    complain_no: str
    complain_remarks: Optional[str]
    complain_status: str
    created_by: str

# FastAPI app
app = FastAPI(title="Task Complaint API", description="CRUD API for managing complaints with SQLModel")

# Create tables on startup
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# Dependency to get database session
def get_session():
    with Session(engine) as session:
        yield session

# CREATE - Add new task/complaint
@app.post("/tasks", response_model=TaskResponse, status_code=201)
def create_task(task: TaskCreate, session: Session = Depends(get_session)):
    """Create a new task/complaint"""
    db_task = Task.model_validate(task)
    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task

# READ - Get all tasks
@app.get("/tasks", response_model=list[TaskResponse])
def list_tasks(
    status: Optional[str] = None,
    created_by: Optional[str] = None,
    skip: int = 0,
    limit: int = 100,
    session: Session = Depends(get_session)
):
    """Get all tasks with optional filtering by status and created_by"""
    statement = select(Task)

    if status:
        statement = statement.where(Task.complain_status == status)
    if created_by:
        statement = statement.where(Task.created_by == created_by)

    statement = statement.offset(skip).limit(limit)
    tasks = session.exec(statement).all()
    return tasks

# READ - Get single task by ID
@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, session: Session = Depends(get_session)):
    """Get a single task by ID"""
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail=f"Task with ID {task_id} not found")
    return task

# UPDATE - Update existing task
@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task_update: TaskUpdate, session: Session = Depends(get_session)):
    """Update an existing task"""
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail=f"Task with ID {task_id} not found")

    # Update only provided fields
    task_data = task_update.model_dump(exclude_unset=True)
    for key, value in task_data.items():
        setattr(task, key, value)

    session.add(task)
    session.commit()
    session.refresh(task)
    return task

# DELETE - Delete task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, session: Session = Depends(get_session)):
    """Delete a task by ID"""
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail=f"Task with ID {task_id} not found")

    session.delete(task)
    session.commit()
    return {"message": "Task deleted successfully", "id": task_id}

# Health check endpoint
@app.get("/")
def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "message": "Task Complaint API is running with SQLModel"}

# Database connection check endpoint
@app.get("/health/db")
def database_health_check(session: Session = Depends(get_session)):
    """Check if database connection is working"""
    try:
        # Try to execute a simple query
        session.exec(select(Task).limit(1))
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Database connection failed: {str(e)}")
