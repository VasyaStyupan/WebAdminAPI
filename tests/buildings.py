from src.base.base_buildings import *


def test_get_entities(signin_ba):
    get_accessed_entities(signin_ba)


def test_get_buildings_as_UA(signin_ua):
    get_building(signin_ua, "ua")


def test_get_building_as_BA(signin_ba):
    get_building(signin_ba, "ba")


def test_get_building_setting(signin_ba):
    get_building_setting(signin_ba)


def test_update_building_setting(signin_ba):
    update_building_setting(signin_ba)


def test_get_building_floors(signin_ba):
    get_building_floors(signin_ba)


def test_update_floors(signin_ba):
    update_floors(signin_ba)


def test_set_floors_quantity(signin_ba):
    set_floors_quantity(signin_ba)


def test_get_rooms_by_buildings(signin_ba):
    get_by_buildings(signin_ba, "rooms")


def test_get_users_by_buildings(signin_ba):
    get_by_buildings(signin_ba, "users")


def test_get_relays_by_buildings(signin_ba):
    get_by_buildings(signin_ba, "relays")


def test_get_doorbells_by_buildings(signin_ba):
    get_by_buildings(signin_ba, "doorbells")
