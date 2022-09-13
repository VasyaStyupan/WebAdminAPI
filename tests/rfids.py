from src.base.base_rfids import *


def test_create_rfid(signin_ba, signin_ua):
    create_rfid(signin_ba, signin_ua)


def test_update_rfid(signin_ba, signin_ua):
    update_rfid(signin_ba, signin_ua)


def test_delete_rfid(signin_ba, signin_ua):
    delete_rfid(signin_ba, signin_ua)
