from flask import Flask
from flask_pytest_example.handlers.routes import configure_routes

def test_home():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/home'
    response = client.get(url)
    assert response.status_code == 200






'''import pytest
from app import create_app

@pytest.fixture
def app():
    app = create_app()
    return app

app.testing = True
client = app.test_client()

@pytest.mark.usefixtures('client_class')
class TestSuite:

    def test_myview(self):
        assert self.client.get(url_for('home')).status_code == 200

import pytest
import requests
from app import create_app

from flask import url_for


@pytest.fixture
def test_home():
    r = requests.get(url_for('home', _external=True))
    assert r.status_code == 200


@pytest.fixture
def app():
    app = create_app()
    return app

def test_app(client):
    assert client.get(url_for('home')).status_code == 200'''