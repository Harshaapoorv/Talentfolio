from app.db.base_class import Base  # <-- ONLY Base is defined there

# Import all models here so Alembic / metadata is aware of them
from app.models.user import UserModel  # noqa: F401