from sqlalchemy import create_engine # type: ignore
from sqlalchemy.orm import sessionmaker # type: ignore
from app.core.config import settings  # your config
from app.db.base import Base  # type: ignore

# engine = create_engine(settings.SQLALCHEMY_DATABASE_URL, future=True)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False}  # <-- Only required for SQLite
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    from app.db.base import Base  # ensure models are imported
    Base.metadata.create_all(bind=engine)