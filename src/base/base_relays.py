import requests
from configuration import BASE_URL
from src.base.base_buildings import get_by_buildings


def get_relay_settings(signin_ba):
    relay_id, building_id = get_by_buildings(signin_ba, "relays")
    resp = requests.get(url=f"{BASE_URL}/buildings/{building_id}/relays/{relay_id}/settings", headers=signin_ba)
    assert resp.status_code == 200, f"Received status code is not equal to expected {resp.status_code}"


def update_relay_settings(signin_ba):
    relay_id, building_id = get_by_buildings(signin_ba, "relays")
    body = {
        "name": "trumtum tum"
    }
    resp = requests.patch(url=f"{BASE_URL}/buildings/{building_id}/relays/{relay_id}/settings", headers=signin_ba,
                          json=body)
    assert resp.status_code == 200, f"Received status code is not equal to expected {resp.status_code}"


def get_user_list_by_relay_access(signin_ba):
    relay_id, building_id = get_by_buildings(signin_ba, "relays")
    resp = requests.get(url=f"{BASE_URL}/buildings/{building_id}/relays/{relay_id}/users", headers=signin_ba)
    assert resp.status_code == 200, f"Received status code is not equal to expected {resp.status_code}"
