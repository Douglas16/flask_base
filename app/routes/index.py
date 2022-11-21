from flask import Blueprint


blueprint = Blueprint('index', __name__)

@blueprint.route("/")
def index():
    return "<p>Hello From Flask</p>"