from flask import Flask

from .db import db
from .routes import routes


def create_app(config_file='settings.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    db.init_app(app)

    app.register_blueprint(routes)

    return app
