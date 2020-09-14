import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


@pytest.fixture(scope='session')
def database():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_database'
    db = SQLAlchemy(app=app)
    db.init_app(app)
    return db

@pytest.fixture(scope='session')
def _db(database):
    return database