from flask import Blueprint, request, current_app, jsonify

from app import get_opc_connected_instance

blueprint = Blueprint('api', __name__, url_prefix='/api')


@blueprint.route('/servers', methods=['GET'])
def get_servers():
    opc = current_app.opc

    return jsonify(opc.servers()) # Retorna a lista de servidores


@blueprint.route('/<server>/info', methods=['GET'])
def get_server_info(server):
    opc = get_opc_connected_instance(server=server) # Conecta no servidor escolhido

    return {info[0]: info[1] for info in opc.info()} # Retorna as infomacoes do servidor formatadas como um dicionario


@blueprint.route('/<server>/items', methods=['GET'])
def get_items(server):
    opc = get_opc_connected_instance(server=server)

    items = opc.read(opc.list(recursive=True)) # Consulta a lista de todos os itens do servidor e realiza a leitura de todos os valores

    return {item[0]: item[1:] for item in items} # Retorna os nomes e valores de todos os itens formatados como um dicionario


@blueprint.route('/<server>/item/<item_name>', methods=['GET'])
def get_single_item(server, item_name):
    opc = get_opc_connected_instance(server=server)

    item = {item_name: opc.read(item_name)} # Realiza a leitura do valor do item escolhido e formata como dicionario

    return item # Retorna o nome e valor do item escolhido



@blueprint.route('/<server>/items', methods=['POST'])
def post_items_value(server):
    opc = get_opc_connected_instance(server)
    data = request.json # Recupera as infomarcoes enviadas no corpo da requisicao

    for key, value in data.items(): # Itera sobre cada items recebido no compro da requisicao
        opc[key] = value # Atribui o valor desejado ao item informado

    items = opc.read(data.keys()) # Realiza a leitura dos itens para os quais foram atribruidos novos valores

    return {item[0]: item[1:] for item in items} # Retorna os nomes e valores dos items modificados
