from config import Config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

# todo: admin localhost i ostalo stavit u config.py
DATABASE_URI = 'postgres+psycopg2://' + Config.PSQL_SERVER_USER + ':' + Config.PSQL_SERVER_PASSWORD + '@' + Config.PSQL_SERVER_HOST + ':' + Config.PSQL_SERVER_PORT + '/' + Config.PSQL_SERVER_DATABASE

engine = create_engine(DATABASE_URI, echo=True)
Session = sessionmaker(bind=engine)


@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
