from flask import Blueprint

app_blueprints = Blueprint('app_blueprints', __name__)
socketio = SocketIO()

from .index import *
