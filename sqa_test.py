from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URI = 'postgres+psycopg2://postgres:admin@localhost:5432/leon_testing'
Base = declarative_base()


class Korisnik(Base):
    __tablename__ = "korisnici"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    def __repr__(self):
        return f"User(username: '{self.username}', password: '{self.password}')"

engine = create_engine(DATABASE_URI, echo=True)
Base.metadata.create_all(engine)


djuro = Korisnik(username='djuro', password='blaaa')

Session = sessionmaker(bind=engine)
session = Session()
session.add(djuro)
session.commit()
