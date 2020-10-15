from flask import Blueprint, request, render_template, json, current_app

from opc_utils import get_opc_connected_instance

blueprint = Blueprint('star-delta', __name__, url_prefix='/star-delta')


@blueprint.route('/visualization', methods=['GET'])
def star_delta_visualization():
    opc = get_opc_connected_instance()

    on_off_switch = json.dumps(opc['Connection1.IN0'])

    on_off_probe = json.dumps(opc['Connection1.OUT0'])

    star_delta_switches = json.dumps({"star1": opc['Connection1.OUT1'],
                                      "star2": opc['Connection1.OUT2'],
                                      "star3": opc['Connection1.OUT3'],
                                      "delta1": opc['Connection1.OUT4'],
                                      "delta2": opc['Connection1.OUT5'],
                                      "delta3": opc['Connection1.OUT6']})

    timer = json.dumps(opc['Connection1.MEMWORD1'])

    return render_template("index.html",
                           on_off_switch=on_off_switch,
                           on_off_probe=on_off_probe,
                           star_delta_switches=star_delta_switches,
                           timer=timer)


@blueprint.route('/connect', methods=['GET'])
def connect_on_server():
    opc = get_opc_connected_instance()

    return {"inputs": {"Starter": opc['Connection1.IN0']},
            "outputs": {"On_Off": opc['Connection1.OUT0'],
                        "Star_1": opc['Connection1.OUT1'],
                        "Star_2": opc['Connection1.OUT2'],
                        "Star_3": opc['Connection1.OUT3'],
                        "Delta_1": opc['Connection1.OUT4'],
                        "Delta_2": opc['Connection1.OUT5'],
                        "Delta_3": opc['Connection1.OUT6']},
            "memory": {"Timer": opc['Connection1.MEMWORD1']}}


@blueprint.route('/', methods=['GET'])
def get_all_values():
    opc = current_app.opc

    return {"inputs": {"Starter": opc['Connection1.IN0']},
            "outputs": {"On_Off": opc['Connection1.OUT0'],
                        "Star_1": opc['Connection1.OUT1'],
                        "Star_2": opc['Connection1.OUT2'],
                        "Star_3": opc['Connection1.OUT3'],
                        "Delta_1": opc['Connection1.OUT4'],
                        "Delta_2": opc['Connection1.OUT5'],
                        "Delta_3": opc['Connection1.OUT6']},
            "memory": {"Timer": opc['Connection1.MEMWORD1']}}


@blueprint.route('/', methods=['POST'])
def set_input():
    opc = get_opc_connected_instance()
    data = request.json

    if type(data) is not bool:
        return {"messsage": "invalid type"}, 400

    opc['Connection1.IN0'] = data

    return {"inputs": {"Starter": opc['Connection1.IN0']},
            "outputs": {"On_Off": opc['Connection1.OUT0'],
                        "Star_1": opc['Connection1.OUT1'],
                        "Star_2": opc['Connection1.OUT2'],
                        "Star_3": opc['Connection1.OUT3'],
                        "Delta_1": opc['Connection1.OUT4'],
                        "Delta_2": opc['Connection1.OUT5'],
                        "Delta_3": opc['Connection1.OUT6']},
            "memory": {"Timer": opc['Connection1.MEMWORD1']}}
