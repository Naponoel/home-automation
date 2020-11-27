from webapp import bcrypt
from webapp.database.session_generator import session_scope
from webapp.database.session_generator import engine
import models

""" Samo korisnici"""
# Base.metadata.drop_all(engine)
models.Base.metadata.create_all(engine)

hashed_password = bcrypt.generate_password_hash('Afg@2t7Dg!sd').decode("utf-8")
admin = models.Korisnici(korisnicko_ime='admin', zaporka=hashed_password)
with session_scope() as sess:
    sess.add(admin)
    sess.commit()

# from webapp.database.session_generator import session_scope
# from webapp.models.microcontrollers import Microcontroller, MicrocontrollerSchema
# with session_scope() as s:
#     controllers = s.query(Microcontroller).all()
#     print(controllers)
