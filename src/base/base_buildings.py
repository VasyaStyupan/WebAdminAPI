import requests
from configuration import BASE_URL
from src.base.base_users import get_own_profile
from src.base.base_rooms import get_by_room


def upload_image(signin_ba, signin_ua):
    user_id, building_id, room_id, rfid_id = get_own_profile(signin_ua)
    doorbell_id = get_by_room(signin_ua, "doorbells")
    files = {
        'image': open('/Users/StyupanVasyl/WebAdminRequests/src/picture.jpeg', 'rb')
    }
    resp = requests.patch(url=f"{BASE_URL}/buildings/{building_id}/doorbells/{doorbell_id}/rooms/{room_id}/image", headers=signin_ba, files=files)
    assert resp.status_code == 200, f"Received status code is not equal to expected {resp.status_code}"


def get_accessed_entities(signin_ba):
    resp = requests.get(url=f"{BASE_URL}/accessed", headers=signin_ba)
    assert resp.status_code == 200, f"Received status code is not equal to expected {resp.status_code}"


def get_building(signin, level):
    resp = requests.get(url=f"{BASE_URL}/{level}/buildings", headers=signin)
    assert resp.status_code == 200, f"Received status code is not equal to expected {resp.status_code}"
    return resp.json()['data'][0]['id']


def get_building_setting(signin_ba):
    building_id = get_building(signin_ba, "ba")
    resp = requests.get(url=f"{BASE_URL}/buildings/{building_id}/settings", headers=signin_ba)
    assert resp.status_code == 200, f"Received status code is not equal to expected {resp.status_code}"


def update_building_setting(signin_ba):
    building_id = get_building(signin_ba, "ba")
    body = {
        "unitAdminAllowCreateUser": False,
        "unitAdminAllowChangeRoomHeader": False,
        "unitAdminAllowCreateUnitAdmin": False,
        "userAllowAddRfid": False,
        "unitAdminAllowUpdateRfid": False
    }
    resp = requests.patch(url=f"{BASE_URL}/buildings/{building_id}/settings", headers=signin_ba, json=body)
    assert resp.status_code == 200, f"Received status code is not equal to expected {resp.status_code}"


def get_building_floors(signin_ba):
    building_id = get_building(signin_ba, "ba")
    resp = requests.get(url=f"{BASE_URL}/buildings/{building_id}/floors",
                        headers=signin_ba)
    assert resp.status_code == 200, f"Received status code is not equal to expected {resp.status_code}"
    id_floors = []
    for i in resp.json()['data']:
        id_floors.append(i['id'])
    return id_floors


def set_floors_quantity(signin_ba):
    building_id = get_building(signin_ba, "ba")
    body = {"floorsCount": 3}
    resp = requests.post(url=f"{BASE_URL}/buildings/{building_id}/floors", headers=signin_ba, json=body)
    assert resp.status_code == 200, f"Received status code is not equal to expected {resp.status_code}"


def update_floors(signin_ba):
    building_id = get_building(signin_ba, "ba")
    id_floors = get_building_floors(signin_ba)
    number = 0
    body = []
    for id_floor in id_floors:
        number += 1
        body.append({
            "id": id_floor,
            "floorName": f"floor {number}",
            "abbreviated": f"abbreviated {number}"
        })
    body = {'floors': body}
    resp = requests.patch(url=f"{BASE_URL}/buildings/{building_id}/floors", headers=signin_ba, json=body)
    assert resp.status_code == 200, f"Received status code is not equal to expected {resp.status_code}"


def get_by_buildings(signin_ba, item):
    building_id = get_building(signin_ba, "ba")
    resp = requests.get(url=f"{BASE_URL}/buildings/{building_id}/{item}", headers=signin_ba)
    assert resp.status_code == 200, f"Received status code is not equal to expected {resp.status_code}"
    return resp.json()['data'][0]['id'], building_id
