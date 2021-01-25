import const
import requests


def test_get_poffers_parking():
    objects = []
    dop_url = 'parking'
    params = {'vid': const.id_car, 'lifetime': '60', 'type': 'garage', 'lat': '11.1', 'lon': '12.2'}
    headers = {'Authorization': const.auth}

    req = requests.get(const.base_url + const.poffers + dop_url, headers=headers, params=params)
    objects.append(req)
    req.json()

    assert 200 == req.status_code
    print(req.json())
    print(objects)

def test_get_poffers_package():
    objects = []
    dop_url = 'package'
    params = {'vid': const.id_car, 'dist': '100', 'dist_units': 'km', 'shared': 'true'}
    headers = {'Authorization': const.auth}

    req = requests.get(const.base_url + const.poffers + dop_url, headers=headers, params=params)
    objects.append(req)
    req.json()

    assert 200 == req.status_code
    print(req.json())
    print(objects)

def test_post_poffers_ride():
    objects = []
    dop_url = 'ride'
    headers = {'Authorization': const.auth, 'Content-Type': 'application/json'}
    # body = {json}

    req = requests.post(const.base_url + const.poffers + dop_url, headers=headers)
    objects.append(req)
    req.json()

    assert 200 == req.status_code
    print(req.json())
    print(objects)

if __name__ == '__main__':
    test_post_poffers_ride()
