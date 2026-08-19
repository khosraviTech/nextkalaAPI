
from sqlalchemy.orm import sessionmaker

from .config import settings

from sqlalchemy import create_engine


engine = create_engine(settings.DATABASE_URL)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
    
)

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()