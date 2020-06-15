from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship

DATABASE_URI = 'postgres+psycopg2://postgres:admin@localhost:5432/leon_testing'
Base = declarative_base()


class Korisnik(Base):
    __tablename__ = "korisnici"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    def __repr__(self):
        return f"User(username: '{self.username}', password: '{self.password}')"


class Kontroler(Base):
    __tablename__ = 'kontroleri'
    id = Column(Integer, primary_key=True)
    children = relationship("Pin", back_populates="parent")


class Pin(Base):
    __tablename__ = 'pinovi'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('kontroleri.id'))
    parent = relationship("Kontroler", back_populates="children")


engine = create_engine(DATABASE_URI, echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
# session.commit()
