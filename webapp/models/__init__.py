from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from models.users import Korisnici
from models.microcontrollers import Microcontroller, Pin
