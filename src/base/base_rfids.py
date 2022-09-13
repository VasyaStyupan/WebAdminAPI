import requests
from configuration import BASE_URL
from src.base.base_users import get_own_profile


def create_rfid(signin_ba, signin_ua):
    user_id, building_id, room_id, rfid_id = get_own_profile(signin_ua)
    body = {
        "rfid": "111111111",
        "name": "first-rfid",
        "roomIds": [1]
    }
    body['roomIds'][0] = room_id
    resp = requests.post(url=f"{BASE_URL}/buildings/{building_id}/users/{user_id}/rfids", headers=signin_ba, json=body)
    assert resp.status_code == 200, f"Received status code is not equal to expected {resp.status_code}"


def update_rfid(signin_ba, signin_ua):
    user_id, building_id, room_id, rfid_id = get_own_profile(signin_ua)
    body = {
        "rfid": "22222222",
        "name": "updated-rfid",
        "roomIds": [1111111]
    }
    body['roomIds'][0] = room_id
    resp = requests.patch(url=f"{BASE_URL}/buildings/{building_id}/users/{user_id}/rfids/{rfid_id}", headers=signin_ba,
                          json=body)
    assert resp.status_code == 200, f"Received status code is not equal to expected {resp.status_code}"


def delete_rfid(signin_ba, signin_ua):
    user_id, building_id, room_id, rfid_id = get_own_profile(signin_ua)
    resp = requests.delete(url=f"{BASE_URL}/buildings/{building_id}/rooms/{room_id}/users/{user_id}/rfids/{rfid_id}", headers=signin_ba)
    assert resp.status_code == 200, f"Received status code is not equal to expected {resp.status_code}"


