import const
import requests


def test_get_vehicles_summary_show():
    objects = []
    headers = {'Authorization': const.auth}
    options = '/summary/'

    req = requests.get(const.base_url + const.vehicles + const.uid + options + const.vid,
                       headers=headers)
    objects.append(req)

    assert 200 == req.status_code
    print(req.json())
    print(objects)

def test_get_vehicles_sharedvehicle_index():
    objects = []
    headers = {'Authorization': const.auth}
    options = '/shared'
    params = {'include': 'all'}

    req = requests.get(const.base_url + const.vehicles + const.uid + options,
                       params=params,
                       headers=headers)
    objects.append(req)

    assert 200 == req.status_code
    print(req.json())
    print(objects)

# def test_get_vehicles_sharedvehicle_summary():
#     objects = []
#     headers = {'Authorization': const.auth}
#     options = '/shared/summary'
#     params = {'include': 'all'}
#
#     req = requests.get(const.base_url + const.vehicles + const.uid + options,
#                        params=params,
#                        headers=headers)
#     objects.append(req)
#
#     assert 200 == req.status_code
#     print(req.json())
#     print(objects)


def test_get_vehicles_sharedvehicle_show():
    objects = []
    headers = {'Authorization': const.auth}
    options = '/shared/'

    req = requests.get(const.base_url + const.vehicles + const.uid + options + const.shared_id,
                       headers=headers)
    objects.append(req)

    assert 200 == req.status_code
    print(req.json())
    print(objects)

# def test_get_vehicles_sharedvehicle_delete():
#     objects = []
#     headers = {'Authorization': const.auth}
#     options = '/shared/'
#
#     req = requests.delete(const.base_url + const.vehicles + const.uid + options + const.shared_id,
#                        headers=headers)
#     objects.append(req)
#
#     assert 200 == req.status_code
#     print(req.json())
#     print(objects)

def test_get_vehicles_own_request_create():
    objects = []
    headers = {'Authorization': const.auth}
    params = {'submit': 'true'}
    options = '/own/'
    options_2 = '/request'

    req = requests.post(const.base_url + const.vehicles + const.uid + options + const.vid + options_2,
                       params=params,
                       headers=headers)
    objects.append(req)

    assert 201 == req.status_code
    print(req.json())
    print(objects)

def test_get_vehicles_own_request_show():
    objects = []
    headers = {'Authorization': const.auth}
    options = '/own/'
    options_2 = '/request'

    req = requests.get(const.base_url + const.vehicles + const.uid + options + const.vid + options_2,
                       headers=headers)
    objects.append(req)

    assert 200 == req.status_code
    print(req.json())
    print(objects)