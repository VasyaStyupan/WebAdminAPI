import requests
from configuration import BASE_URL, CHANGE_ROOM_BODY
from src.base.base_users import get_own_profile


def get_by_room(signin, level):
    user_id, building_id, room_id, rfid_id = get_own_profile(signin)
    resp = requests.get(url=f"{BASE_URL}/buildings/{building_id}/rooms/{room_id}/{level}", headers=signin)
    assert resp.status_code == 200, f"Received status code is not equal to expected {resp.status_code}"
    return resp.json()['data'][0]['id']


def get_room_settings(signin_ua):
    user_id, building_id, room_id, rfid_id = get_own_profile(signin_ua)
    resp = requests.get(url=f"{BASE_URL}/buildings/{building_id}/rooms/{room_id}/settings", headers=signin_ua)
    assert resp.status_code == 200, f"Received status code is not equal to expected {resp.status_code}"


def update_room(signin_ua, signin_ba):
    user_id, building_id, room_id, rfid_id = get_own_profile(signin_ua)
    resp = requests.patch(url=f"{BASE_URL}/buildings/{building_id}/rooms/{room_id}/settings", headers=signin_ba,
                          json=CHANGE_ROOM_BODY)
    assert resp.status_code == 200, f"Received status code is not equal to expected {resp.status_code}"


def change_users_room_restriction(signin_ua, signin_ba):
    user_id, building_id, room_id, rfid_id = get_own_profile(signin_ua)
    body = {
        "enableAppDoor": True,
        "enableDoorbellButton": True
    }
    resp = requests.patch(url=f"{BASE_URL}/buildings/{building_id}/rooms/{room_id}/users/{user_id}", headers=signin_ba,
                          json=body)
    assert resp.status_code == 200, f"Received status code is not equal to expected {resp.status_code}"
