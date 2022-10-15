from src.base.base_rooms import *


def test_get_relays_by_room(signin_ua):
    get_by_room(signin_ua, "relays")


def test_get_users_by_room(signin_ua):
    get_by_room(signin_ua, "users")


def test_get_doorbells_by_room(signin_ua):
    get_by_room(signin_ua, "doorbells")


def test_get_room_settings(signin_ua):
    get_room_settings(signin_ua)


def test_update_room(signin_ua, signin_ba):
    update_room(signin_ua, signin_ba)


def test_change_users_room_restriction(signin_ua, signin_ba):
    change_users_room_restriction(signin_ua, signin_ba)
