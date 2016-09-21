from pytest import fixture

from app import create_app, db


@fixture
def test_client(app):
    yield app.test_client()


@fixture
def app():
    app = create_app('testing')
    yield app
    db.drop_all(app=app)
