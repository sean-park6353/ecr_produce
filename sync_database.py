from sqlalchemy import create_engine
from sqlalchemy.ext import declarative
import contextlib
from sqlalchemy.orm import sessionmaker
import os 

MYSQL_URL =  os.getenv("MYSQL_URL")
engine = create_engine(MYSQL_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative()
@contextlib.contextmanager
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()