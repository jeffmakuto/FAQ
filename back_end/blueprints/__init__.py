from flask import Blueprint
from flask_socketio import SocketIO

app_blueprints = Blueprint('app_blueprints', __name__)
socketio = SocketIO()

from .index import *
