from flask import Blueprint

app_blueprints = Blueprint('app_blueprints', __name__)

from .index import *
