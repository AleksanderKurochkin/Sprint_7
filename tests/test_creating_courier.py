import requests
import pytest
import allure
from data import CreatingCourier, Url, BodyResponse


class TestCreatingCourier:
    @allure.title('Тест создания курьера')
    @allure.description('Генерируем рандомный логин и передаем запрос с корректными параметрами, проверяем код 201 и тело '
                        'ответа')
    def test_creating_courier(self):
        data = CreatingCourier.creating_new_courier
        response = requests.post(f'{Url.HOST}/courier', json=data)

        assert response.status_code == 201 and response.json() == BodyResponse.MESSAGE_201

    @allure.title('Тест нельзя создать двух одинаковых курьеров')
    @allure.description('В данных передаем логин который был ранее зарегистрирован, проверяем код 409 и тело'
                        'ответа')
    def test_creating_courier_double(self):
        data = CreatingCourier.creating_double_courier
        response = requests.post(f'{Url.HOST}/courier', json=data)

        assert response.status_code == 409 and response.json() == BodyResponse.MESSAGE_409

    @allure.title('Тест если одного из обязательных полей нет, запрос возвращает ошибку')
    @allure.description('В данных передаем данные сначала без логина потом без пароля, проверяем код 400 и тело'
                        'ответа')
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_creating_courier_missing_field(self, missing_field):
        data = CreatingCourier.creating_new_courier
        del data[missing_field]
        response = requests.post(f'{Url.HOST}/courier', json=data)

        assert response.status_code == 400 and response.json() == BodyResponse.MESSAGE_400
