# from pathlib import Path
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from sqlalchemy import Column, Integer, String
# from flask_login import UserMixin
from flask import current_app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# from webapp import login_manager

server_pw = current_app.config['PSQL_SERVER_PASSWORD']
srv_host = current_app.config['PSQL_SERVER_HOST']
srv_port = current_app.config['PSQL_SERVER_PORT']
srv_db = current_app.config['PSQL_SERVER_DATABASE']

DATABASE_URI = f'postgres+psycopg2://postgres:{server_pw}@{srv_host}:{srv_port}/{srv_db}'
Base = declarative_base()


# @login_manager.user_loader
# def load_user(user_id):
#     sess = PSQL_Session()
#     return sess.query(User).get(int(user_id))


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    def __repr__(self):
        return f"User(username: '{self.username}', password: '{self.password}')"


class Device(Base):
    __tablename__ = "devices"
    id = Column(Integer, primary_key=True)
    description = Column(String, unique=True, nullable=False)
    location = Column(String, nullable=False)
    # param1 = Column(String, nullable=False)
    # param2 = Column(String, nullable=False)
    # param3 = Column(String, nullable=False)
    # param4 = Column(String, nullable=False)
    # param5 = Column(String, nullable=False)
    # param6 = Column(String, nullable=False)
    # param7 = Column(String, nullable=False)

    def __repr__(self):
        return f"Device(description: '{self.description}', location: '{self.location}')"


engine = create_engine(DATABASE_URI, echo=True)
Base.metadata.create_all(engine)
PSQL_Session = sessionmaker(bind=engine)
