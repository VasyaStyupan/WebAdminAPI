import requests
from src.base.base_users import get_own_profile
from configuration import BASE_URL


def get_layout_options(signin_ua):
    user_id, building_id, room_id, rfid_id = get_own_profile(signin_ua)
    resp = requests.get(url=f"{BASE_URL}/arx/buildings/{building_id}/room-access-categories", headers=signin_ua)
    assert resp.status_code == 200, f"Received status code is not equal to expected {resp.status_code}"
    print(resp.json())
