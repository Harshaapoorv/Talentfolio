from fastapi import FastAPI # type: ignore
from app.api import db_test

app = FastAPI()

app.include_router(db_test.router)

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/users")
def get_users():
    return [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]