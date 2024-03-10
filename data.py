from faker import Faker


class CreatingCourier:
    fake = Faker()
    login = fake.user_name()
    creating_new_courier = {
        "login": login,
        "password": "1234",
        "firstName": "Александр"
    }

    creating_double_courier = {
        "login": "SashaKurochkin",
        "password": "1234",
        "firstName": "Александр"
    }


class Url:
    HOST = 'https://qa-scooter.praktikum-services.ru/api/v1'


class BodyResponse:
    MESSAGE_409 = {"code": 409,
                   "message": "Этот логин уже используется. "
                              "Попробуйте другой."}
    MESSAGE_404 = {"code": 404,
                   "message": "Учетная запись не найдена"}

    MESSAGE_400 = {"code": 400,
                   "message": "Недостаточно данных для создания учетной записи"}
    MESSAGE_400_LOGIN = {"code": 400,
                         "message": "Недостаточно данных для входа"}

    MESSAGE_201 = {"ok": True}


class Authentication:
    courier_authentication = {
        "login": "SashaKurochkin",
        "password": "1234",
    }
