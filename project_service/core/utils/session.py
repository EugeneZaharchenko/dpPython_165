from contextlib import contextmanager

import sqlalchemy
from sqlalchemy.orm import sessionmaker

from ..config import postgres_uri


engine = sqlalchemy.create_engine(postgres_uri())
Session = sessionmaker(bind=engine)


@contextmanager
def session(auto_commit=True):
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        if auto_commit:
            session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
