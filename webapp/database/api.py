from flask import Blueprint, request
from flask_login import login_required
from webapp.database.session_generator import session_scope
from models import Microcontroller, Pin
import json

api = Blueprint("api", __name__)


@api.route('/get-controllers', methods=['POST'])
@login_required
def get_controllers():
    controlers = dict()
    pair = dict()
    pin_list = list()
    main_list = list()
    with session_scope() as s:
        query = s.query(Microcontroller).all()
        if query:
            for controler in query:
                for pin in controler.pins:
                    pin_list.append(pin.serialize())
                controler_info = controler.serialize()
                pair['controller_info'] = controler_info
                pair['pins'] = pin_list
                main_list.append(pair)
            return json.dumps(main_list)
    return json.dumps(controlers)


@api.route('/update-controller-name', methods=['POST'])
@login_required
def update_controller_name():
    with session_scope() as s:
        uC = s.query(Microcontroller).filter_by(mac_address=str(request.form["controler_id"])).one()
        uC.controller_name = request.form["new_name"]
        s.commit()
    return {'response': 200}


@api.route('/get-active-microcontrollers', methods=['POST'])
@login_required
def get_active_microcontrollers():
    controlers = dict()
    pins = dict()
    main_dict = dict()
    with session_scope() as s:
        query = s.query(Microcontroller).filter_by(active=True).all()
        if query:
            for controler in query:
                controlers[controler.mac_address] = controler.serialize()
                for pin in controler.pins:
                    if pin.active is True and pin.io_type == "OUTPUT":
                        pins[pin.embeded_pin_name] = pin.serialize()
                main_dict[controler.mac_address] = pins
            return json.dumps(main_dict)
        else:
            return json.dumps({'response': 'NoActiveMicrocontrollers'})


@api.route('/activate-microcontroller', methods=['POST'])
@login_required
def activate_microcontroller():
    with session_scope() as s:
        uC = s.query(Microcontroller).filter_by(mac_address=str(request.form["controler_id"])).one()
        uC.active = True
        s.add(uC)
        s.commit()
    return {'response': 200}


@api.route('/activate-pin', methods=['POST'])
@login_required
def activate_pin():
    with session_scope() as s:
        pin = s.query(Pin).filter_by(id=str(request.form["element_id"])).one()
        pin.active = True
        s.add(pin)
        s.commit()
    return {'response': 200}


@api.route('/deactivate-pin', methods=['POST'])
@login_required
def deactivate_pin():
    with session_scope() as s:
        pin = s.query(Pin).filter_by(id=str(request.form["element_id"])).one()
        pin.active = False
        s.add(pin)
        s.commit()
    return {'response': 200}


@api.route('/deactivate-microcontroller', methods=['POST'])
@login_required
def deactivate_microcontroller():
    with session_scope() as s:
        uC = s.query(Microcontroller).filter_by(mac_address=str(request.form["controler_id"])).one()
        uC.active = False
        s.add(uC)
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
