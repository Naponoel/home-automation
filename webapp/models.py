from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from flask_login import UserMixin

Base = declarative_base()


class Korisnik(Base, UserMixin):
    __tablename__ = "korisnici"
    id = Column(Integer, primary_key=True)
    korisnicko_ime = Column(String, unique=False, nullable=False)
    zaporka = Column(String, nullable=False)

    def __repr__(self):
        return f"Korisnik(ime: '{self.korisnicko_ime}', zaporka: 'pitaj_konobara'"


class Kontroler(Base):
    __tablename__ = 'kontroleri'
    id = Column(Integer, primary_key=True)
    komponenta = Column(String, unique=False)
    # P u Pin je velko jer referenciramo python klasu
    pinovi = relationship('Pin', backref='parent_kontroler', lazy=True)

    def __repr__(self):
        return f"Kontroler(komponenta: '{self.komponenta}', Pinovi: '{self.pinovi}'"


class Pin(Base):
    __tablename__ = 'pinovi'
    id = Column(Integer, primary_key=True)
    # kontroler.id je malo jer referenciramo SQL table i column
    kontroler_id = Column(Integer, ForeignKey('kontroleri.id'), nullable=False)
    oznaka_pina = Column(String, unique=False)

    def __repr__(self):
        return f"Pin(oznaka_pina: '{self.oznaka_pina}', parent_component: '{self.kontroler_id}'"
