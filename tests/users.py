from src.base.base_users import *


def test_get_search(signin_ba):
    get_search(signin_ba)


def test_get_own_profile(signin_ua):
    get_own_profile(signin_ua)


def test_get_user_details(signin_ua):
    get_user_details(signin_ua)


def test_update_user_profile(signin_ua):
    update_user_profile(signin_ua)


def test_create_and_delete_user_in_unit(signin_ba, signin_ua):
    create_user_in_unit(signin_ba, signin_ua)








