from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from webapp import marsh
from marshmallow import fields

Base = declarative_base()


class Korisnik(Base, UserMixin):
    __tablename__ = "korisnici"
    id = Column(Integer, primary_key=True)
    korisnicko_ime = Column(String, unique=False, nullable=False)
    zaporka = Column(String, nullable=False)

    def __repr__(self):
        return f"Korisnik(ime: '{self.korisnicko_ime}', zaporka: 'pitaj_konobara'"


class KorisnikSchema(marsh.Schema):
    # todo: napravit kao i kod KontrolerSchema
    class Meta:
        model = Korisnik


class Kontroler(Base):
    __tablename__ = 'kontroleri'
    id = Column(Integer, primary_key=True)
    lokacija = Column(String, unique=False)
    LAN_IP = Column(String, unique=False)
    # P u Pin je velko jer referenciramo python klasu
    pinovi = relationship('Pin', backref='parent_kontroler', lazy=True)

    def __repr__(self):
        return f"Kontroler(" \
               f"lokacija: '{self.lokacija}', " \
               f"LAN_IP: '{self.LAN_IP}'," \
               f"Pinovi: '{self.pinovi}'"


class KontrolerSchema(marsh.Schema):
    id = fields.Int(dump_only=True)
    komponenta = fields.Str()


class Pin(Base):
    __tablename__ = 'pinovi'
    id = Column(Integer, primary_key=True)
    # kontroler.id je malo jer referenciramo SQL table i column
    pripada_komponenti = Column(Integer, ForeignKey('kontroleri.id'), nullable=False)
    oznaka_pina = Column(String, unique=False)
    funkcija_pina = Column(String, unique=False)

    def __repr__(self):
        return f"Pin(" \
               f"oznaka_pina: '{self.oznaka_pina}'," \
               f"pripada_komponenti: '{self.pripada_komponenti}'" \
               f"funkcija_pina: '{self.funkcija_pina}'"


class PinSchema(marsh.Schema):
    class Meta:
        model = Pin
