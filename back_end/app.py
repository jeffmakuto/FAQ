from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from blueprints import app_blueprints
import os

app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/*":{'origins':'*'}})

# Global strict slashes
app.url_map.strict_slashes = False

# Register blueprint
app.register_blueprint(app_blueprints)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
