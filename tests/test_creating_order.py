import requests
import pytest
import allure

class TestCreatingOrder:
    @allure.title('Тест указаания цвета в запросе')
    @allure.description('В данных передаем цвет или пустое поле, проверяем код 201 и что тело'
                        'ответа содержит track')
    @pytest.mark.parametrize("color", [
        "BLACK",
        "GREY",
        "BLACK, GREY",
        ""
    ])
    def test_courier_orders(self, color):
        data = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 2,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": [color]
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', json=data)

        assert response.status_code == 201 and "track" in response.json()
