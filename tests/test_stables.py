import requests
import const
import time


def test_get_stables_grz():
    objects = []
    number = 'Н504АР799'
    options = 'plates/ru/'
    headers = {'Authorization': const.auth}

    req = requests.get(const.base_url + const.stables + options + number, headers=headers)
    objects.append(req)
    req.json()
    time.sleep(5)
    req = requests.get(const.base_url + const.stables + options + number, headers=headers)

    assert 200 == req.status_code
    print(req.json())
    print(objects)

def test_get_stables_vin():
    objects = []
    vin = "WBANA71030B605898"
    options = "vin/"
    headers = {'Authorization': const.auth}

    req = requests.get(const.base_url + const.stables + options + vin, headers=headers)
    objects.append(req)
    req.json()
    time.sleep(5)
    req = requests.get(const.base_url + const.stables + options + vin, headers=headers)

    assert 200 == req.status_code
    print(req.json())
    print(objects)


if __name__ == '__main__':
    test_get_stables_grz()