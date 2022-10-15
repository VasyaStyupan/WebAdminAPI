import requests
from configuration import BASE_URL, DORBELL_BODY, DOORBELL_CHANGE_BODY, CUSTOM_DAY_BODY, CUSTOM_DAY_UNIT_BODY
from configuration import CUSTOM_DAY_CHANGE_BODY, UPDATE_PARTY_MODE_BODY, CUSTOM_DAY_UNIT_CHANGE_BODY
from src.base.base_buildings import get_building, get_by_buildings
from src.base.base_users import get_own_profile
from src.base.base_rooms import get_by_room


def get_doorbell_settings(signin):
    building_id, doorbell_id = get_doorbell(signin, "ua")
    resp = requests.get(url=f"{BASE_URL}/buildings/{building_id}/doorbells/{doorbell_id}/settings", headers=signin)
    assert resp.status_code == 200, f"Received status code is not equal to expected {resp.status_code}"


def get_doorbell(signin, level):
    resp = requests.get(url=f"{BASE_URL}/{level}/doorbells", headers=signin)
    assert resp.status_code == 200, f"Received status code is not equal to expected {resp.status_code}"
    building_id = resp.json()['data'][0]['buildingId']
    doorbell_id = resp.json()['data'][0]['id']
    return building_id, doorbell_id


def get_room_doorbell_settings(signin):
    building_id, doorbell_id = get_doorbell(signin, "ua")
    user_id, building_id, room_id, rfid_id = get_own_profile(signin)
    resp = requests.get(url=f"{BASE_URL}/buildings/{building_id}/rooms/{room_id}/doorbells/{doorbell_id}/settings",
                        headers=signin)
    assert resp.status_code == 200, f"Received status code is not equal to expected {resp.status_code}"


def update_doorbell(signin_ba, signin_ua):
    building_id, doorbell_id = get_doorbell(signin_ua, "ua")
    resp = requests.patch(url=f"{BASE_URL}/buildings/{building_id}/doorbells/{doorbell_id}/settings", headers=signin_ba,
                          json=DORBELL_BODY)
    assert resp.status_code == 200, f"Received status code is not equal to expected {resp.status_code}"


def change_room_doorbell_settings(signin_ba, signin_ua):
    building_id, doorbell_id = get_doorbell(signin_ua, "ua")
    user_id, building_id, room_id, rfid_id = get_own_profile(signin_ua)
    resp = requests.patch(url=f"{BASE_URL}/buildings/{building_id}/rooms/{room_id}/doorbells/{doorbell_id}/settings",
                          headers=signin_ba, json=DOORBELL_CHANGE_BODY)
    assert resp.status_code == 200, f"Received status code is not equal to expected {resp.status_code}"


def create_custom_day(signin):
    doorbell_id, building_id = get_by_buildings(signin, "doorbells")
    resp = requests.post(url=f"{BASE_URL}/buildings/{building_id}/doorbells/{doorbell_id}/customday", headers=signin,
                         json=CUSTOM_DAY_BODY)
    assert resp.status_code == 200, f"Received status code is not equal to expected {resp.status_code}"
    customday_id = resp.json()['id']
    return building_id, doorbell_id, customday_id


def get_custom_day_by_range_for_doorbell(signin):
    doorbell_id, building_id = get_by_buildings(signin, "doorbells")
    resp = requests.get(
        url=f"{BASE_URL}/buildings/{building_id}/doorbells/{doorbell_id}?start=2022.09.01&end=2022.09.30",
        headers=signin)
    assert resp.status_code == 200, f"Received status code is not equal to expected {resp.status_code}"
    customday_id = resp.json()['customDays'][0]['id']
    return building_id, doorbell_id, customday_id


def change_custom_day_by_range_for_doorbell(signin):
    building_id, doorbell_id, customday_id = get_custom_day_by_range_for_doorbell(signin)
    resp = requests.patch(url=f"{BASE_URL}/buildings/{building_id}/doorbells/{doorbell_id}/customday/{customday_id}",
                          headers=signin, json=CUSTOM_DAY_CHANGE_BODY)
    assert resp.status_code == 200, f"Received status code is not equal to expected {resp.status_code}"


def delete_custom_day_by_range_for_doorbell(signin):
    doorbell_id, building_id = get_by_buildings(signin, "doorbells")
    resp = requests.delete(
        url=f"{BASE_URL}/buildings/{building_id}/doorbells/{doorbell_id}?start=2022.09.01&end=2022.09.30",
        headers=signin)
    assert resp.status_code == 200, f"Received status code is not equal to expected {resp.status_code}"


def create_custom_day_by_range_for_doorbell_unit_level(signin_ba, signin_ua):
    user_id, building_id, room_id, rfid_id = get_own_profile(signin_ua)
    doorbell_id = get_by_room(signin_ua, "doorbells")
    resp = requests.post(url=f"{BASE_URL}/buildings/{building_id}/doorbells/{doorbell_id}/rooms/{room_id}/customday",
                         headers=signin_ba,
                         json=CUSTOM_DAY_UNIT_BODY)
    assert resp.status_code == 200, f"Received status code is not equal to expected {resp.status_code}"
    customday_id = resp.json()['id']
    return building_id, doorbell_id, room_id, customday_id


def get_custom_day_by_range_for_doorbell_unit_level(signin_ua):
    user_id, building_id, room_id, rfid_id = get_own_profile(signin_ua)
    doorbell_id = get_by_room(signin_ua, "doorbells")
    resp = requests.get(
        url=f"{BASE_URL}/buildings/{building_id}/doorbells/{doorbell_id}/rooms/{room_id}?start=2022.09.01&end=2022.09.30",
        headers=signin_ua)
    assert resp.status_code == 200, f"Received status code is not equal to expected {resp.status_code}"
    customday_id = resp.json()['customDays'][0]['id']
    return building_id, doorbell_id, room_id, customday_id


def change_custom_day_by_range_for_doorbell_unit_level(signin_ba, signin_ua):
    building_id, doorbell_id, room_id, customday_id = get_custom_day_by_range_for_doorbell_unit_level(signin_ua)
    resp = requests.patch(
        url=f"{BASE_URL}/buildings/{building_id}/doorbells/{doorbell_id}/rooms/{room_id}/customday/{customday_id}",
        headers=signin_ba, json=CUSTOM_DAY_UNIT_CHANGE_BODY)
    assert resp.status_code == 200, f"Received status code is not equal to expected {resp.status_code}"


def delete_custom_day_by_range_for_doorbell_unit_level(signin_ua):
    user_id, building_id, room_id, rfid_id = get_own_profile(signin_ua)
    doorbell_id = get_by_room(signin_ua, "doorbells")
    resp = requests.delete(
        url=f"{BASE_URL}/buildings/{building_id}/doorbells/{doorbell_id}/rooms/{room_id}?start=2022.09.01&end=2022.09.30",
        headers=signin_ua)
    assert resp.status_code == 200, f"Received status code is not equal to expected {resp.status_code}"


def delete_custom_day_doorbell_level(signin_ba):
    building_id, doorbell_id, customday_id = create_custom_day(signin_ba)
    resp = requests.delete(url=f"{BASE_URL}/buildings/{building_id}/doorbells/{doorbell_id}/customday/{customday_id}",
                           headers=signin_ba)
    assert resp.status_code == 200, f"Received status code is not equal to expected {resp.status_code}"


def delete_custom_day_doorbell_unit_level(signin_ba, signin_ua):
    building_id, doorbell_id, room_id, customday_id = create_custom_day_by_range_for_doorbell_unit_level(signin_ba, signin_ua)
    resp = requests.delete(
        url=f"{BASE_URL}/buildings/{building_id}/doorbells/{doorbell_id}/rooms/{room_id}/customday/{customday_id}",
        headers=signin_ua)
    assert resp.status_code == 200, f"Received status code is not equal to expected {resp.status_code}"


def update_party_mode_schedule_on_room_level(signin_ba, signin_ua):
    building_id, doorbell_id, room_id, customday_id = get_custom_day_by_range_for_doorbell_unit_level(signin_ua)
    resp = requests.patch(
        url=f"{BASE_URL}/buildings/{building_id}/rooms/{room_id}/doorbells/{doorbell_id}/schedule",
        headers=signin_ba, json=UPDATE_PARTY_MODE_BODY)
    assert resp.status_code == 200, f"Received status code is not equal to expected {resp.status_code}"


def update_party_mode_schedule_on_doorbell_level(signin_ba):
    building_id, doorbell_id, customday_id = create_custom_day(signin_ba)
    resp = requests.patch(
        url=f"{BASE_URL}/buildings/{building_id}/doorbells/{doorbell_id}/schedule",
        headers=signin_ba, json=UPDATE_PARTY_MODE_BODY)
    assert resp.status_code == 200, f"Received status code is not equal to expected {resp.status_code}"
    delete_custom_day_by_range_for_doorbell(signin_ba)
