from fastapi import FastAPI # type: ignore

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/users")
def get_users():
    return [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]