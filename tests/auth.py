import pytest
from src.base.base_auth import login
from configuration import CODE, USERNAME, PASSWORD


@pytest.mark.parametrize('username, password, code, status', [
    # Log in with valid login & valid password
    (USERNAME, PASSWORD, CODE, 200),
    # Log in with valid login in upper case & valid password
    (USERNAME.upper(), PASSWORD, CODE, 200),
    # Log in with valid login with spaces & valid password (less than 6 characters)
    (f" {USERNAME} ", PASSWORD, CODE, 200),
    # Log in with valid login  & valid password with spaces
    (USERNAME, f" {PASSWORD} ", CODE, 200),
    # Log in with valid login  & valid password in upper case
    (USERNAME, PASSWORD.upper(), CODE, 401),
    # Log in with valid login & invalid password
    (USERNAME, PASSWORD[:6], CODE, 401),
    # Log in with valid login  & invalid password (less than 6 characters)
    (USERNAME, PASSWORD[:5], CODE, 410),
    # Log in with invalid login &valid password
    (USERNAME[:5], PASSWORD, CODE, 401),
    # Log in with empty fields
    ("", "", CODE, 410),
    # Log in with empty login  & valid password
    ("", PASSWORD, CODE, 401),
    # Log in with valid login  & empty password
    (USERNAME, "", CODE, 410),
])
def test_signin(username, password, code, status):
    login(username, password, code, status)

