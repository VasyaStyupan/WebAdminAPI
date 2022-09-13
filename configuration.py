BASE_URL = "https://webrtc.defigohome.com/ca"
SIGNIN_URL = "https://webrtc.defigohome.com/ca/signin"
CODE_URL = "https://webrtc.defigohome.com/ca/signin/code"

USERNAME_BA = "building@ma.nager"
PASSWORD_BA = "Qwerty1"

USERNAME_UA = "manager@te.st"
PASSWORD_UA = "Qwerty123"

USERNAME = USERNAME_UA
PASSWORD = PASSWORD_UA  # minimum 7 symbols
CODE = "1111"

CREATE_USER_BODY = {
    'userName': 'JohnDoe',
    'fName': 'John',
    'lName': 'Doe',
    'email': 'mymail@gmail.com',
    'phone': '0123456789',
    'countryCode': '47',
    'isBuildingAdmin': False,
    'isUnitAdmin': True,
    'isUnitOwner': False
}

DELETE_USER_BODY = {
    "fName": "John",
    "lName": "Doe",
    "userName": "JohnDoe",
    "email": "mymail@gmail.com",
    "phone": "0123456789"
}
CHANGE_ROOM_BODY = {
    "header": "dontdeletethisunit",
    "uid": "fortest",
    "floorId": 2
}

DORBELL_BODY = {
    "publicName": "Vet Test Emak 1",
    "hiddenButtons": True,
    "hiddenSearchBar": True,
    "screenBrightness": 50,
    "volume": 25,
    "showPersonalImg": True,
    "showRoomImg": True,
    "partyMode": "schedule",
    "enforceFamilyMode": True,
    "unitAdminAllowPersonalImg": True,
    "unitAdminAllowRoomImg": True,
    "unitAdminAllowUploadImg": True,
    "unitAdminAllowPartyMode": True,
    "userAllowAddRfid": True,
    "isPinRequired": True
}

DOORBELL_CHANGE_BODY = {
    "showPersonalImg": True,
    "showRoomImg": True,
    "isDoorbellScheduleShown": True,
    "isUsersConstraintUsed": True,
    # "disabled": True
}

CUSTOM_DAY_BODY = {
    "startTime": "10:00",
    "endTime": "22:00",
    "isPartyModeEnabled": True,
    "date": "2022.09.14"
}
CUSTOM_DAY_CHANGE_BODY = {
    "startTime": "9:00",
    "endTime": "20:00",
    "isPartyModeEnabled": True,
    "date": "2022.09.14"
}
CUSTOM_DAY_UNIT_BODY = {
    "startTime": "7:00",
    "endTime": "8:00",
    "isPartyModeEnabled": False,
    "date": "2022.09.14"
}

CUSTOM_DAY_UNIT_CHANGE_BODY = {
    "startTime": "7:00",
    "endTime": "8:00",
    "isPartyModeEnabled": True,
    "date": "2022.09.14"
}

UPDATE_PARTY_MODE_BODY = {
    "schedule": [
        {
            "dayOfWeek": "0",
            "startTime": "00:10:00",
            "endTime": "2:00:00",
            "isPartyModeEnabled": False
        },
        {
            "dayOfWeek": "1",
            "startTime": "3:50:00",
            "endTime": "4:00:00",
            "isPartyModeEnabled": True
        },
        {
            "dayOfWeek": "2",
            "startTime": "5:00:00",
            "endTime": "6:00:00",
            "isPartyModeEnabled": True
        },
        {
            "dayOfWeek": "3",
            "startTime": "7:00:00",
            "endTime": "8:00:00",
            "isPartyModeEnabled": True
        },
        {
            "dayOfWeek": "4",
            "startTime": "9:00:00",
            "endTime": "10:00:00",
            "isPartyModeEnabled": True
        }
    ]
}
