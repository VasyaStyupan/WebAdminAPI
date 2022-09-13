import requests
from configuration import BASE_URL, CREATE_USER_BODY, DELETE_USER_BODY, USERNAME_UA


def get_search(signin_ba):
    resp = requests.get(url=f"{BASE_URL}/search?search={USERNAME_UA}", headers=signin_ba)
    result = resp.json()['total']
    if result != 0:
        user_id = resp.json()['data'][0]['userId']
        building_id = resp.json()['data'][0]['buildingId']
    else:
        user_id = 0
        building_id = 0
    return user_id, building_id


def get_own_profile(signin_ua):
    resp = requests.get(url=f"{BASE_URL}/profile", headers=signin_ua)
    assert resp.status_code == 200, f"Received status code is not equal to expected {resp.status_code}"
    user_id = resp.json()['id']
    building_id = resp.json()['rooms'][0]['building']['id']
    room_id = resp.json()['rooms'][0]['id']
    try:
        rfid_id = resp.json()['rfids'][0]['id']
    except IndexError:
        rfid_id = 0
    return user_id, building_id, room_id, rfid_id


def get_user_details(signin_ua):
    user_id = get_own_profile(signin_ua)[0]
    resp = requests.get(url=f"{BASE_URL}/users/{user_id}", headers=signin_ua)
    assert resp.status_code == 200, f"Received status code is not equal to expected {resp.status_code}"
    return (resp.json()['userName'])


def get_list_of_phone_codes(signin_ua):
    resp = requests.get(url=f"{BASE_URL}/phone_codes?search=norw&limit=2&offset=2", headers=signin_ua)
    assert resp.status_code == 200, f"Received status code is not equal to expected {resp.status_code}"
    return


def update_user_profile(signin_ua):
    user_id = get_own_profile(signin_ua)[0]
    body = {
        'fName': 'First name',
        'lName': 'Last name',
        'email': 'new@email.com',
        'phone': '1234567890',
        'countryCode': '47'
    }
    resp = requests.patch(url=f"{BASE_URL}/users/{user_id}", headers=signin_ua, json=body)
    assert resp.status_code == 200, f"Received status code is not equal to expected {resp.status_code}"
    return


def create_user_in_unit(signin_ba):
    user_id, building_id, room_id, rfid_id = get_own_profile(signin_ba)

    resp = requests.post(url=f"{BASE_URL}/buildings/{building_id}/rooms/{room_id}/users", headers=signin_ba,
                         json=CREATE_USER_BODY)
    assert resp.status_code == 200, f"Received status code is not equal to expected {resp.status_code}"


def remove_user_from_unit(signin_ba):
    user_id, building_id, room_id, rfid_id = get_own_profile(signin_ba)
    result, user_id = get_search(signin_ba)
    resp = requests.delete(url=f"{BASE_URL}/buildings/{building_id}/rooms/{room_id}/users/{user_id}",
                               headers=signin_ba, json=DELETE_USER_BODY)
    assert resp.status_code == 200, f"Received status code is not equal to expected {resp.status_code}"
