import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Login" in response.data  # page has Login heading

def test_login_fail(client):
    response = client.post("/login", json={
        "username": "wronguser",
        "password": "wrongpass"
    })
    assert response.status_code == 401
    assert b"Invalid username or password" in response.data

def test_create_catalogue(client):
    response = client.post("/catalogues", json={
        "catalogue_name": "TestCat",
        "catalogue_description": "Test Description",
        "start_date": "2025-07-01",
        "end_date": "2025-07-31"
    })
    assert response.status_code in [201, 400]  # 400 if already exists
