# app/api/db_test.py
from fastapi import APIRouter, Depends # type: ignore
from sqlalchemy.orm import Session # type: ignore
from sqlalchemy import text # type: ignore
from fastapi.responses import JSONResponse as JSONIFY # type: ignore
from app.db.session import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/db-test")
def db_test(id: int, db: Session = Depends(get_db)):
    value = db.execute(text("SELECT name FROM test_table WHERE id=:id"), {"id": id}).scalar()
    if value is None:
        return JSONIFY(status_code=404, content={"error": "Record not found"})
    return {"db": "connected", "value": value}

@router.post("/db-test-insert")
def db_test_insert(name: str, db: Session = Depends(get_db)):
    db.execute(text("INSERT INTO test_table (name) VALUES (:name)"), {"name": name})
    db.commit()
    return {"status": "inserted", "name": name}

@router.delete("/db-test-clear")
def db_test_clear(db: Session = Depends(get_db)):
    db.execute(text("DELETE FROM test_table"))
    db.commit()
    return {"status": "cleared"}

@router.put("/db-test-update")
def db_test_update(id: int, name: str, db: Session = Depends(get_db)):
    result = db.execute(text("UPDATE test_table SET name=:name WHERE id=:id"), {"name": name, "id": id})
    db.commit()
    if result.rowcount == 0:
        return JSONIFY(status_code=404, content={"error": "Record not found"})
    return {"status": "updated", "id": id, "name": name}
