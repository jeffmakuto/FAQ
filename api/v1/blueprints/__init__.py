from flask import Blueprint

app_blueprints = Blueprint('app_blueprints', __name__, url_prefix='/api/v1')

from .index import *
