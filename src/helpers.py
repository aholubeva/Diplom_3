import faker
import requests
from src.config import Config

def register_new_user():
    fake = faker.Faker()
    email = fake.email()
    password = fake.password()
    name = fake.name()

    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    response = requests.post(f"{Config.URL}/api/auth/register", data=payload)

    if response.status_code == 200:
        return email, password

def get_sign_in_data():
    email = "anastasiyagolubeva13123@yandex.ru"
    password = "123456"
    return email, password