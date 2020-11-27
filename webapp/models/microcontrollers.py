from sqlalchemy import Column, Integer, String, Boolean, Float
from models import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Microcontroller(Base):
    __tablename__ = "microcontrollers"
    id = Column(Integer, primary_key=True)
    mac_address = Column(String, nullable=False, unique=True)
    controller_name = Column(String, nullable=True)
    active = Column(Boolean)

    pins = relationship("Pin", back_populates="parent_microcontroller")

    def serialize(self):
        return {
            'id': self.id,
            'mac_address': self.mac_address,
            'controller_name': self.controller_name,
            'active': self.active
        }


class Pin(Base):
    __tablename__ = "pins"
    id = Column(Integer, primary_key=True)
    embeded_pin_name = Column(String, nullable=False)
    used_for = Column(String, nullable=True)
    io_type = Column(String)
    active = Column(Boolean)
    current_value = Column(Float)

    parent_id = Column(Integer, ForeignKey('microcontrollers.id'))
    parent_microcontroller = relationship("Microcontroller", back_populates="pins")