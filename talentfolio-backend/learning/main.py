from fastapi import FastAPI
from pydantic import BaseModel, Field

class User(BaseModel):
    name: str
    email: str
    age: int

class Update_user(BaseModel):
    name: str | None = None
    email: str | None = None
    age: int | None = None

class Task(BaseModel):
    title: str
    description: str | None = None
    priority: int = 1

class Product(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    price: float = Field(..., gt=0)
    stock: int = Field(default=0, ge=0)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the Learning Module!"}

@app.get("/hello/{name}")
def say_hello(name: str):
    if (len(name) < 2) or len(name) > 50:
        return {"status": "error", "message": "Name must be between 2 and 50 characters long."}
    return {"message": f"Hello, {name}!"}

@app.get("/hello")
def say_hello_query_param(name: str):
    if len(name) < 2 or len(name) > 50:
        return {"status": "error", "message": "Name must be between 2 and 50 characters long."}
    return {"message": f"Hello, {name}!"}

@app.get("/user/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "message": "User details retrieved successfully through path params."}

@app.get("/search")
def search(query: str, limit: int = 10):
    return {"query": query, "limit": limit, "message": "Search executed successfully through query params."}

@app.post("/create-user")
def create_user(user: User):
    return {"message": "User created successfully.", "data": user}

@app.put("/update-user/{user_id}")
def update_user(user_id: int, user:Update_user):
    return {"message": "User updated successfully.", "user_id": user_id, "updated_data": user}

@app.post("/create-item")
def create_item(item: User, notify: bool = False):
    return {"item": item, "notify": notify, "message": "Item created successfully with optional notification."}

@app.post("/projects/{project_id}/tasks")
def create_task(project_id: int, task: Task, completed: bool = False, urgent: bool = False):
    if (task.priority < 1) or task.priority > 5: 
        return {"status": "error", "message": "Priority must be between 1 and 5."}
    return {
        "project_id": project_id,
        "task": task,
        "completed": completed,
        "urgent": urgent,
        "message": "Task created successfully under the specified project."
    }

@app.post("/product")
def create_product(product: Product):
    return {"message": "Product created successfully.", "data": product}