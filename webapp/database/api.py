from flask import Blueprint, request
from flask_login import login_required
from webapp.database.session_generator import session_scope
from models import Microcontroller, Pin

api = Blueprint("api", __name__)


@api.route('/uninitialised-controllers', methods=['POST'])
@login_required
def uninitialised_controllers():
    controlers = list()
    with session_scope() as s:
        query = s.query(Microcontroller).filter_by(active=False).all()
        if query:
            for controler in query:
                controlers.append(controler.serialize())
    print(controlers)
    return {'response': controlers}


@api.route('/update-controller-name', methods=['POST'])
@login_required
def update_controller_name():
    print(request.form["new_name"])
    with session_scope() as s:
        uC = s.query(Microcontroller).filter_by(mac_address=str(request.form["controler_id"])).one()
        uC.controller_name = request.form["new_name"]
        s.commit()
    return {'response': 200}


# @api.route('/add-new-controller', methods=['POST'])
# @login_required
# def create_controller():
#     s = Session()
#     new_controller = Kontroler(komponenta=request.form['Naziv komponente'], lokacija=request.form['Lokacija'], lan_ip=request.form['LAN IP'])
#     s.add(new_controller)
#     s.commit()
#     s.close()
#     return {'response': 200}


# @api.route('/delete-controller', methods=['POST'])
# @login_required
# def delete_controller():
#     s = Session()
#     print(request.form['komponenta'])
#     kontroler = s.query(Kontroler).filter_by(id=request.form['sqlID']).delete()
#     # s.delete(kontroler)
#     s.commit()
#     s.close()
#     return {'response': 200}


# @api.route('/get-controllers')
# @login_required
# def get_controllers():
#     s = Session()
#     kontroleri = s.query(Kontroler).all()
#     s.close()
#     return {'response': serialize_json(kontroleri, KontrolerSchema(many=True))}


# @api.route('/controller-update', methods=['POST'])
# @login_required
# def update_controllers():
#     s = Session()
#     s.query(Kontroler).filter(Kontroler.id == request.form['sqlID']).update(
#         {request.form['subsection']: request.form['newValue']})
#     s.commit()
#     updated_controller = s.query(Kontroler).filter(Kontroler.id == request.form['sqlID']).first()
#     s.close()
#     return {'changedSection': request.form['subsection'],
#             'response': serialize_json(updated_controller, KontrolerSchema(many=False))}


# @api.route('/switch', methods=['POST'])
# @login_required
# def switch_pin_state():
#     pin_state = 0
#     mqtt.publish('/sub', "{\"type\":\"requestCommand\", \"PR1\":%d}" % pin_state)
#     return "yas"


def serialize_json(query, schema_obj):
    sch = schema_obj
    return sch.dump(query)
