from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from Amanda import DB_URI


def start() -> scoped_session:
    engine = create_engine(DB_URI, pool_size=20, max_overflow=20, client_encoding="utf8")
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=True, autocommit=False, expire_on_commit=True, info=None))


BASE = declarative_base()
SESSION = start()
