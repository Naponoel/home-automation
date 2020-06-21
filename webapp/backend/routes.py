from flask import Blueprint, request
from flask_login import login_required
from webapp.models import Kontroler
from webapp.database import Session
from webapp.models import KontrolerSchema

backend = Blueprint("backend", __name__)


@backend.route('/add-new-controller', methods=['POST'])
@login_required
def create_controller():
    s = Session()
    new_controller = Kontroler(komponenta=request.form['Naziv komponente'], lokacija=request.form['Lokacija'], lan_ip=request.form['LAN IP'])
    s.add(new_controller)
    s.commit()
    s.close()
    return {'response': 200}


@backend.route('/get-controllers')
@login_required
def get_controllers():
    s = Session()
    kontroleri = s.query(Kontroler).all()
    s.close()
    return {'response': serialize_json(kontroleri, KontrolerSchema(many=True))}


@backend.route('/controller-update', methods=['POST'])
@login_required
def update_controllers():
    s = Session()
    s.query(Kontroler).filter(Kontroler.id == request.form['sqlID']).update(
        {request.form['subsection']: request.form['newValue']})
    s.commit()
    updated_controller = s.query(Kontroler).filter(Kontroler.id == request.form['sqlID']).first()
    s.close()
    return {'changedSection': request.form['subsection'],
            'response': serialize_json(updated_controller, KontrolerSchema(many=False))}


def serialize_json(query, schema_obj):
    sch = schema_obj
    return sch.dump(query)
