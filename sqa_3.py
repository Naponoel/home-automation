from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship

DATABASE_URI = 'postgres+psycopg2://postgres:admin@localhost:5432/zavrsni'
Base = declarative_base()


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


engine = create_engine(DATABASE_URI, echo=True)
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

esp1 = Kontroler(komponenta='esp8266-kuhinja')
GPIO1 = Pin(kontroler_id=esp1.id, oznaka_pina='GPIO-kuhinja-svijetlo')
GPIO2 = Pin(kontroler_id=esp1.id, oznaka_pina='GPIO-kupaona-ventilator')

esp1.pinovi = [GPIO1, GPIO2]

session.add(esp1)
# a = session.query(Kontroler).filter(Kontroler.komponenta=='esp8266-kuhinja').all()
# a = a[1]
# a.pinovi
# a.pinovi[1].parent_kontroler

session.commit()
session.close()
print('end')
