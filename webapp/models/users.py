from sqlalchemy import Column, Integer, String
from flask_login import UserMixin
from models import Base


class Korisnici(Base, UserMixin):
    __tablename__ = "korisnici"
    id = Column(Integer, primary_key=True)
    korisnicko_ime = Column(String, unique=False, nullable=False)
    zaporka = Column(String, nullable=False)

    def __repr__(self):
        return f"Korisnik(ime: '{self.korisnicko_ime}')"
