from flask import Flask, current_app
import OpenOPC


def create_app():
    # Funcao responsavel por inicializar a aplicacao REST
    app = Flask(__name__)
    app.threaded = False
    __register_blueprints(app)
    app.opc = OpenOPC.client()

    return app


def __register_blueprints(app):
    from views.api import blueprint
    from views.star_delta_visualization import blueprint as star_delta_blueprint


    app.register_blueprint(blueprint) # Registra na aplicacao os endpoints definidos no arquivo api.py
    app.register_blueprint(star_delta_blueprint) # Registra na aplicacao os endpoints definidos no arquivo star_delta.py


def get_opc_connected_instance(server):
    # Funcao auxiliar que retorna uma instancia do cliente OpenOPC conectada no servidor passado no argumento
    opc = current_app.opc
    opc.connect(server)

    return opc
