from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from blueprints import app_blueprints
import os

app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/*":{'origins':}})

# Global strict slashes
app.url_map.strict_slashes = False

# Configure templates and static folders for the web application
app.template_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'front_end', 'bot_vue', 'public'))
app.static_folder= os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'front_end', 'bot_vue', 'src'))

# Register blueprint
app.register_blueprint(app_blueprints)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
