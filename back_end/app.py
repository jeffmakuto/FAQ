#!/usr/bin/env python3
"""
Bot's Flask application with SocketIO support.
"""

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO
from blueprints import app_blueprints

app = Flask(__name__)
CORS(app, resources={r"/*": {'origins': '*'}})
app.url_map.strict_slashes = False
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app, cors_allowed_origins="*")

app.register_blueprint(app_blueprints)


if __name__ == '__main__':
    """
    Entry point for the application. Runs the Flask app with SocketIO support.
    """
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)

