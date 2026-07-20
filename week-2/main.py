from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel


# Create FastAPI application
app = FastAPI()


# Model used when a user creates a new task
class TaskCreate(BaseModel):
    title: str


# Temporary in-memory task storage
tasks = [
    {
        "id": 1,
        "title": "Learn FastAPI",
        "done": False
    },
    {
        "id": 2,
        "title": "Complete Week 2 Assignment",
        "done": False
    }
]


# Root endpoint
@app.get("/")
def home():
    return {
        "message": "Task API is running",
        "docs": "/docs"
    }


# Health check endpoint
@app.get("/health")
def health():
    return {
        "status": "ok"
    }


# Get all tasks
@app.get("/tasks")
def get_tasks():
    return tasks


# Get a single task by ID
@app.get("/tasks/{task_id}")
def get_task(task_id: int):

    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )


# Create a new task
@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):

    # Check if the title is empty or contains only spaces
    if not task.title.strip():
        raise HTTPException(
            status_code=400,
            detail="Title cannot be empty"
        )

    # Generate the next available task ID
    new_id = max(
        (existing_task["id"] for existing_task in tasks),
        default=0
    ) + 1

    # Create the new task
    new_task = {
        "id": new_id,
        "title": task.title,
        "done": False
    }

    # Add the new task to our temporary storage
    tasks.append(new_task)

    # Return the newly created task
    return new_task