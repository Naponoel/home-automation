from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class KontrolerForm(FlaskForm):
    lokacija = StringField('Lokacija', validators=[DataRequired('Lokacija je obavezna.')])
    LAN_ip = StringField('LAN_ip', validators=[DataRequired('LAN IP je obavezan.')])
    funkcija_pina = StringField('funkcija_pina', validators=[DataRequired('Funkcija pina je obavezna.')])
    submit = SubmitField('Dodaj novi kontroler')
