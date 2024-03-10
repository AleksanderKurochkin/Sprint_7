import requests
import allure
from data import Url


class TestListOrder:
    @allure.title('Тест получения списка заказов')
    @allure.description('Получаем список заказов без ID, проверяем код 200 и что тело'
                        'ответа содержит orders')
    def test_get_list_order(self):
        response_get = requests.get(f'{Url.HOST}/orders')

        assert response_get.status_code == 200 and "orders" in response_get.json()
