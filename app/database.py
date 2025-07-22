from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session

DATABASE_URL: str = "sqlite:///./wallet_info.db"

engine: Engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal: sessionmaker[Session] = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

Base = declarative_base()

