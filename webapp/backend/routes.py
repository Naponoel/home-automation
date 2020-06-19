from flask import Blueprint, request
from flask_login import login_required
from webapp.models import Kontroler
from webapp.database import Session
from webapp.models import KontrolerSchema

backend = Blueprint("backend", __name__)


@backend.route('/get-controllers')
@login_required
def get_controllers():
    s = Session()
    kontroleri = s.query(Kontroler).all()
    kontroler_schema = KontrolerSchema(many=True)
    out = kontroler_schema.dump(kontroleri)
    return {'response': out}


@backend.route('/controller-update', methods=['POST'])
@login_required
def update_controllers():
    # todo: update SQLAlchemy, SQLAlchemy querry i return novih vrijednosti
    print(request.form)
    return 'success'
