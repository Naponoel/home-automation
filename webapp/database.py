from webapp.models import Korisnik, Kontroler, Pin, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from webapp import login_manager, bcrypt

DATABASE_URI = 'postgres+psycopg2://postgres:admin@localhost:5432/zavrsni'

engine = create_engine(DATABASE_URI, echo=True)
# Base.metadata.drop_all(engine)  # todo: zakomentiraj ako ne koristis
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

# hashed_password = bcrypt.generate_password_hash('admin').decode("utf-8")
# djuro = Korisnik(korisnicko_ime='admin', zaporka=hashed_password)
# a = Session()
# a.add(djuro)
# a.commit()
# a.close()

@login_manager.user_loader
def load_user(user_id):
    sess = Session()
    return sess.query(Korisnik).get(int(user_id))

# esp1 = Kontroler(komponenta='esp8266-kuhinja')
# GPIO1 = Pin(kontroler_id=esp1.id, oznaka_pina='GPIO-kuhinja-svijetlo')
# GPIO2 = Pin(kontroler_id=esp1.id, oznaka_pina='GPIO-kupaona-ventilator')
#
# esp1.pinovi = [GPIO1, GPIO2]
#
# session.add(esp1)
# a = session.query(Kontroler).filter(Kontroler.komponenta=='esp8266-kuhinja').all()
# a = a[1]
# a.pinovi
# a.pinovi[1].parent_kontroler

# session.commit()
# session.close()
