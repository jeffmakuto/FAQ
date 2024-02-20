# back_end/app.py
from flask import Flask
from flask_cors import CORS
from blueprints import app_blueprints
from celery import Celery

app = Flask(__name__)
app.config.from_object(__name__)

# Load Celery configuration from celery_config.py
app.config.from_object('celery_config')

# Initialize Celery
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

CORS(app, resources={r"/*": {'origins': '*'}})
app.url_map.strict_slashes = False
app.register_blueprint(app_blueprints)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
