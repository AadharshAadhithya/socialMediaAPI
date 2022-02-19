from sqlalchemy import create_engine
from app.main import app
from fastapi.testclient import TestClient
from app.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.database import get_db, Base
import pytest

from alembic import command

SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:6karpagam@localhost:5432/fastapi_test"

#SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)


#client = TestClient(app)

@pytest.fixture
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture
def client(session):
    # BEFORE CODE RUNS
    def override_get_db():

        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = override_get_db

    # command.upgrade("head")

    yield TestClient(app)
    # command.downgrade("base")
    # AFTER CODE RUNS
