from conftest import send_user_pass, get_token, send_code


def login(username, password, code, status):
    response = send_user_pass(username, password)
    assert response.status_code == status, f"Received status code is not equal to expected {response.status_code}"
    if response.status_code == 200:
        token = get_token(response)
        response = send_code(code, token)
        token = get_token(response)
        return token
