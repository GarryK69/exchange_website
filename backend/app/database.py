from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:garry@localhost:5432/postgres"  # Укажите вашу базу данных

Base = declarative_base()

engine = create_engine(
    url=SQLALCHEMY_DATABASE_URL,
    echo=True,
    pool_size=15,
    max_overflow=30,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
