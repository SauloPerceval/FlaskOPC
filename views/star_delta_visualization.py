from flask import Blueprint, request, render_template


blueprint = Blueprint('star-delta-visualization', __name__, url_prefix='/star-delta')


@blueprint.route('/', methods=['GET'])
def star_delta_visualization():
    return render_template("star_delta_view.html") # Exibe a pagina web do arquivo star_delta_view.html
