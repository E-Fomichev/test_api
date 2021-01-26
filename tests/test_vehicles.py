import const
import requests


def test_get_vehicles_summary():
    objects = []
    headers = {'Authorization': const.auth}
    options = '/summary/'

    req = requests.get(const.base_url + const.vehicles + const.uid + options + const.vid, headers=headers)
    objects.append(req)

    assert 200 == req.status_code
    print(req.json())
    print(objects)

def test_get_vehicles_sharedvehicle_index():
    objects = []
    headers = {'Authorization': const.auth}
    options = '/shared'
    params = {'include': 'all'}

    req = requests.get(const.base_url + const.vehicles + const.uid + options, params=params, headers=headers)
    objects.append(req)

    assert 200 == req.status_code
    print(req.json())
    print(objects)