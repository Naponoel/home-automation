from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship

DATABASE_URI = 'postgres+psycopg2://postgres:admin@localhost:5432/leon_testing'
Base = declarative_base()


# class Korisnik(Base):
#     __tablename__ = "korisnici"
#     id = Column(Integer, primary_key=True)
#     username = Column(String, unique=True, nullable=False)
#     password = Column(String, nullable=False)
#
#     def __repr__(self):
#         return f"User(username: '{self.username}', password: '{self.password}')"
#
#
class Kontroler(Base):
    __tablename__ = 'kontroler'
    id = Column(Integer, primary_key=True)
    naziv_komponente = Column(String, unique=False, nullable=False)
    pins = relationship('Pin', back_populates='parent_component')

    def __repr__(self):
        return f"Kontroler(Komponenta: '{self.naziv_komponente}', " \
               f"Pinovi: '{self.pins})"


class Pin(Base):
    __tablename__ = 'pin'
    id = Column(Integer, primary_key=True)
    pin_number = Column(Integer, unique=False, nullable=False)
    parent_component = Column(Integer, ForeignKey('kontroler.naziv_komponente'))
    # parent_component_id = Column(Integer, ForeignKey('kontroler.id'))

    def __repr__(self):
        return f"Pin(Pin Number: '{self.pin_number}', " \
               f"Parent Component: '{self.parent_component})"


esp1 = Kontroler(naziv_komponente='esp8266')
print(esp1)

GPIO1 = Pin(pin_number=1)
GPIO2 = Pin(pin_number=3)

esp1 = [Pin(pin_number=1), Pin(pin_number=3)]

print(esp1.naziv_komponente)

# pin_ventilator = Pin(za_komponentu='ventilator', lokacija='kuhinja')
# pin_lampa = Pin(za_komponentu='LED', lokacija='hodnik')
#
# esp1 = Kontroler(lokacija='kuhinja')
#
# pin_lampa.parent_id = esp1.id
# pin_ventilator.parent_id = esp1.id

# esp1 = Kontroler(lokacija='spavaca')
# esp1.pinovi = [Pin('temperatura'), Pin('ventilator')]

# class Parent(Base):
#     __tablename__ = 'parent'
#     id = Column(Integer, primary_key=True)
#     children = relationship("Child", backref="parent")
#
#
# class Child(Base):
#     __tablename__ = 'child'
#     id = Column(Integer, primary_key=True)
#     parent_id = Column(Integer, ForeignKey('parent.id'))
#
#
# p1 = Parent()
# p1.children = [Child()]

engine = create_engine(DATABASE_URI, echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)


esp1.pins.append(GPIO1)


session = Session()
session.add(esp1)
session.commit()
session.close()
# esp1 = Kontroler(naziv_komponente='esp8266')
# GPIO1 = Pin(pin_number=1)
# GPIO2 = Pin(pin_number=3)
print(esp1)
print(GPIO1.parent_component)
