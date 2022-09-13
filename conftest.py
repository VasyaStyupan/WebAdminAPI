import requests
import pytest
from configuration import SIGNIN_URL, CODE_URL, CODE
from configuration import USERNAME_BA, USERNAME_UA, PASSWORD_BA, PASSWORD_UA


def send_user_pass(username, password):  # Sending login & password
    credentials = {"payload": username, "password": password}
    response = requests.post(url=SIGNIN_URL, json=credentials)
    return response


def get_token(response):  # Receiving token for Authorization
    bearer_token = response.json()["accessToken"]
    token = {
        'Authorization': f"Bearer {bearer_token}",
    }
    return token


def send_code(code, token):  # Sending token & code
    secret_code = {"secretCode": code}
    response = requests.post(url=CODE_URL, headers=token, json=secret_code)
    return response


@pytest.fixture
def signin_ba():
    response = send_user_pass(USERNAME_BA, PASSWORD_BA)
    token = get_token(response)
    response = send_code(CODE, token)
    token = get_token(response)
    return token


@pytest.fixture(scope='session')
def signin_ua():
    response = send_user_pass(USERNAME_UA, PASSWORD_UA)
    token = get_token(response)
    response = send_code(CODE, token)
    token = get_token(response)
    return token
