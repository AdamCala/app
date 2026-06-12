import pytest
from app import app, add, greet, reverse


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_add():
    assert add(2, 3) == 5


def test_greet():
    assert greet("Adam") == "Hello, Adam!"


def test_reverse():
    assert reverse("abc") == "cba"


def test_index(client):
    rv = client.get('/')
    assert b'Flask Demo' in rv.data


def test_api_add(client):
    rv = client.get('/api/add?a=2&b=4')
    assert rv.status_code == 200
    assert rv.get_json()['result'] == 6
