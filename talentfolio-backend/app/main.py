from fastapi import FastAPI # type: ignore
from app.api import db_test
from app.db.session import init_db

app = FastAPI()

app.include_router(db_test.router)

@app.on_event("startup")
async def startup_event():
    init_db()


@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/users")
def get_users():
    return [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]