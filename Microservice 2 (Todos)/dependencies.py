from typing import Generator

from database import SessionLocal


def get_db() -> Generator:
    """
    Generator dependency yield database connection.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
