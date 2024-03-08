from faker import Faker
import requests
import pytest
import allure
fake = Faker()


class TestCreatingCourier:
    @allure.title('Тест создания курьера')
    @allure.description('Генерируем рандомный логин и передаем запрос с корректными параметрами, проверяем код 201 и тело '
                        'ответа')
    def test_creating_courier(self):
        login = fake.user_name()
        data = {
            "login": login,
            "password": "1234",
            "firstName": "Aleksander"}
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', json=data)

        assert response.status_code == 201 and response.json() == {"ok": True}

    @allure.title('Тест нельзя создать двух одинаковых курьеров')
    @allure.description('В данных передаем логин который был ранее зарегистрирован, проверяем код 409 и тело'
                        'ответа')
    def test_creating_courier_double(self):
        data = {
            "login": "SashaKurochkin",
            "password": "1234",
            "firstName": "Александр"
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', json=data)

        assert response.status_code == 409 and response.json() == {"code": 409,
                                                                   "message": "Этот логин уже используется. "
                                                                              "Попробуйте другой."}

    @allure.title('Тест если одного из обязательных полей нет, запрос возвращает ошибку')
    @allure.description('В данных передаем данные сначала без логина потом без пароля, проверяем код 400 и тело'
                        'ответа')
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_creating_courier_missing_field(self, missing_field):
        login = fake.user_name()
        data = {
            "login": login,
            "password": "1234",
            "firstName": "Александр"
        }
        del data[missing_field]
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', json=data)

        assert response.status_code == 400 and response.json() == {"code": 400,
                                                                   "message": "Недостаточно данных для создания учетной записи"}
