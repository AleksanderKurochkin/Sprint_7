import pytest
import requests


@pytest.fixture
def courier_authentication_success():
    data = {
        "login": "SashaKurochkin",
        "password": "1234"
    }
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', json=data)

    return response.json()["id"]

