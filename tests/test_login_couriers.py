import requests
import pytest
import allure
from data import Url, Authentication, BodyResponse
class TestLoginCouriers:
    @allure.title('Тест курьер может авторизоваться')
    @allure.description('Передаем корректные данные, проверяем код 200 и что тело'
                        'ответа содержит id курьера')
    def test_courier_authentication_success(self):
        data = Authentication.courier_authentication
        response = requests.post(f'{Url.HOST}/courier/login', json=data)

        assert response.status_code == 200 and "id" in response.json()

    @allure.title('Тест если при авторизации какого-то поля нет, запрос возвращает ошибку 400')
    @allure.description('Передаем данные сначала без пароля потом без логина, проверяем код и что тело'
                        'ответа содержит "Недостаточно данных для входа"')
    @pytest.mark.parametrize("login, password", [
        ("SashaKurochkin", ""),
        ("", "1234")
        ])
    def test_authentication_without_login_or_password(self, login, password):
        data = {
            "login": login,
            "password": password
        }
        response = requests.post(f'{Url.HOST}/courier/login',json=data)

        assert response.status_code == 400 and response.json() == BodyResponse.MESSAGE_400_LOGIN

    @allure.title('Тест если авторизоваться под несуществующим пользователем, запрос возвращает ошибку')
    @allure.description('Передаем несуществующий логин, пароль проверяем код 404 и что тело'
                        'ответа содержит "Недостаточно данных для входа"')
    @pytest.mark.parametrize("login, password", [
        ("SashaKurochkin", "password1234"),
        ("nonexistent_user", "1234"),
        ("nonexistent_user", "wrong_password")
    ])
    def test_authentication_with_invalid_credentials(self, login, password):
        data = {
            "login": login,
            "password": password
        }
        response = requests.post(f'{Url.HOST}/courier/login',json=data )

        assert response.status_code == 404 and response.json() == BodyResponse.MESSAGE_404






