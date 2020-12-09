from flask import Blueprint, request, jsonify
from flask_login import login_required
from webapp.database.session_generator import session_scope
from models import Microcontroller, Pin
import json
from webapp import mqtt

api = Blueprint("api", __name__)


@api.route('/get-controllers', methods=['POST'])
@login_required
def get_controllers():
    controllers = dict()
    pair = dict()
    pin_list = list()
    main_list = list()
    with session_scope() as s:
        query = s.query(Microcontroller).all()
        if query:
            for controller in query:
                for pin in controller.pins:
                    pin_list.append(pin.serialize())
                controler_info = controller.serialize()
                pair['controller_info'] = controler_info
                pair['pins'] = pin_list
                main_list.append(pair)
            return json.dumps(main_list)
    return json.dumps(controllers)


@api.route('/update-controller-name', methods=['POST'])
@login_required
def update_controller_name():
    with session_scope() as s:
        uC = s.query(Microcontroller).filter_by(mac_address=str(request.form["controler_id"])).one()
        uC.controller_name = request.form["new_name"]
        s.commit()
    return jsonify(success=True)


@api.route('/get-active-microcontrollers', methods=['POST'])
@login_required
def get_active_microcontrollers():
    controlers = dict()
    pair = dict()
    pin_list = list()
    main_list = list()
    with session_scope() as s:
        query = s.query(Microcontroller).all()
        if query:
            for controler in query:
                for pin in controler.pins:
                    if pin.active is True and pin.io_type == "OUTPUT":
                        pin_list.append(pin.serialize())
                controler_info = controler.serialize()
                pair['controller_info'] = controler_info
                pair['pins'] = pin_list
                main_list.append(pair)
            return json.dumps(main_list)
    return json.dumps(controlers)


@api.route('/activate-microcontroller', methods=['POST'])
@login_required
def activate_microcontroller():
    with session_scope() as s:
        uC = s.query(Microcontroller).filter_by(mac_address=str(request.form["controler_id"])).one()
        uC.active = True
        s.add(uC)
        s.commit()
    return jsonify(success=True)


@api.route('/activate-pin', methods=['POST'])
@login_required
def activate_pin():
    with session_scope() as s:
        pin = s.query(Pin).filter_by(id=str(request.form["element_id"])).one()
        pin.active = True
        if request.form["friendly_name"]:
            pin.used_for = str(request.form["friendly_name"])
        s.add(pin)
        s.commit()
    return jsonify(success=True)


@api.route('/deactivate-pin', methods=['POST'])
@login_required
def deactivate_pin():
    with session_scope() as s:
        pin = s.query(Pin).filter_by(id=str(request.form["element_id"])).one()
        pin.active = False
        s.add(pin)
        s.commit()
    return jsonify(success=True)


@api.route('/deactivate-microcontroller', methods=['POST'])
@login_required
def deactivate_microcontroller():
    with session_scope() as s:
        uC = s.query(Microcontroller).filter_by(mac_address=str(request.form["controler_id"])).one()
        uC.active = False
        s.add(uC)
        s.commit()
    return jsonify(success=True)


@api.route('/switch-pin-state', methods=['POST'])
@login_required
def switch_pin_state():
    # todo: Upis u bazu ne od ovdije nego preko DB.py
    topic = request.form["controller_mac"] + '/commands'
    pin_embeded_name = request.form["embeded_id"]
    command_value = int(request.form["wanted_pin_value"])
    if "PMW" in pin_embeded_name:
        if command_value == 1:
            command_value = 250
    # command_string in format:
    # "{\"type\":\"requestCommand\", \"PR1\":1}"
    command_string = '{\"type\":\"requestCommand\", \"' + pin_embeded_name + '\":' + str(command_value) + '}'
    mqtt.publish(topic=topic, payload=command_string)

    with session_scope() as s:
        pin = s.query(Pin).filter_by(id=request.form["pin_id"]).one()
        pin.current_value = command_value
        s.add(pin)
        s.commit()
    return {"new_value": command_value}


@api.route('/get-pin-state', methods=['POST'])
@login_required
def get_pin_state():
    with session_scope() as s:
        pin = s.query(Pin).filter_by(id=str(request.form["pin_id"])).one()
        current_state = pin.current_value
    return {"db_state": current_state}


def serialize_json(query, schema_obj):
    sch = schema_obj
    return sch.dump(query)
