from src.base.base_doorbells import *


def test_get_doorbell_settings(signin_ua):
    get_doorbell_settings(signin_ua)


def test_get_doorbell_with_coordinates_as_BA(signin_ba):
    get_doorbell(signin_ba, "ba")


def test_get_doorbell_with_coordinates_as_UA(signin_ua):
    get_doorbell(signin_ua, "ua")


def test_get_room_doorbell_settings(signin_ua):
    get_room_doorbell_settings(signin_ua)


def test_update_doorbell(signin_ba):
    update_doorbell(signin_ba)


def test_change_room_doorbell_settings(signin_ua):
    change_room_doorbell_settings(signin_ua)


def test_create_custom_day_party_doorbell_level(signin_ba):
    create_custom_day(signin_ba)


def test_get_custom_day_by_range_for_doorbell_level(signin_ba):
    get_custom_day_by_range_for_doorbell(signin_ba)


def test_change_custom_day_by_range_for_doorbell(signin_ba):
    change_custom_day_by_range_for_doorbell(signin_ba)


def test_delete_custom_day_by_range_for_doorbell_level(signin_ba):
    delete_custom_day_by_range_for_doorbell(signin_ba)


def test_create_custom_day_party_unit_doorbell_level(signin_ua):
    create_custom_day_by_range_for_doorbell_unit_level(signin_ua)


def test_get_custom_day_by_range_for_doorbell_unit_level(signin_ua):
    get_custom_day_by_range_for_doorbell_unit_level(signin_ua)


def test_change_custom_day_by_range_for_doorbell_unit_level(signin_ua):
    change_custom_day_by_range_for_doorbell_unit_level(signin_ua)


def test_delete_custom_day_by_range_for_doorbell_unit_level(signin_ua):
    delete_custom_day_by_range_for_doorbell_unit_level(signin_ua)


def test_delete_custom_day_doorbell_level(signin_ba):
    delete_custom_day_doorbell_level(signin_ba)


def test_delete_custom_day_doorbell_unit_level(signin_ua):
    delete_custom_day_doorbell_unit_level(signin_ua)


def test_update_party_mode_schedule_on_room_level(signin_ua):
    update_party_mode_schedule_on_room_level(signin_ua)


def test_update_party_mode_schedule_on_doorbell_level(signin_ba):
    update_party_mode_schedule_on_doorbell_level(signin_ba)
