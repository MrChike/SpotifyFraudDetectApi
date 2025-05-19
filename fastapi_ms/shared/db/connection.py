from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from shared.configs.settings import app_settings as AppSettings

DATABASE_URL = AppSettings.database_url

if not DATABASE_URL:
    raise ValueError("DATABASE_URL must be set in the application settings.")

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

# Dependency for FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
