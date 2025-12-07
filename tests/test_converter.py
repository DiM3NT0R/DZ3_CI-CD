import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_distance_km_to_mi(client):
    response = client.get('/distance?value=10&from=km&to=mi')
    assert response.status_code == 200
    assert round(response.json['result'], 2) == 6.21

def test_temperature_c_to_f(client):
    response = client.get('/temperature?value=0&from=C&to=F')
    assert response.status_code == 200
    assert response.json['result'] == 32

def test_weight_kg_to_lb(client):
    response = client.get('/weight?value=1&from=kg&to=lb')
    assert response.status_code == 200
    assert round(response.json['result'], 2) == 2.20

def test_invalid_input(client):
    response = client.get('/distance?value=abc&from=km&to=mi')
    assert response.status_code == 400
    assert 'error' in response.json
