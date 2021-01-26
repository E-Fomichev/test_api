import const
import requests


def test_get_vehiclesbase_makes():
    objects = []
    options = 'makes'

    req = requests.get(const.base_url + const.vehiclesbase + options)
    objects.append(req)
    # model = "10"

    assert 200 == req.status_code
    print(req.json())
    print(objects)


def test_get_vehiclesbase_models():
    objects = []
    options = "models/10"

    req = requests.get(const.base_url + const.vehiclesbase + options)
    objects.append(req)

    assert 200 == req.status_code
    print(req.json())
    print(objects)

def test_get_vehiclesbase_generation():
    objects = []
    options = "generation/84"

    req = requests.get(const.base_url + const.vehiclesbase + options)
    objects.append(req)

    assert 200 == req.status_code
    print(req.json())
    print(objects)

def test_get_vehiclesbase_series():
    objects = []
    options = "series/66"

    req = requests.get(const.base_url + const.vehiclesbase + options)
    objects.append(req)

    assert 200 == req.status_code
    print(req.json())
    print(objects)

def test_get_vehiclesbase_modification():
    objects = []
    options = "modification/14873"

    req = requests.get(const.base_url + const.vehiclesbase + options)
    objects.append(req)

    assert 200 == req.status_code
    print(req.json())
    print(objects)

def test_get_vehiclesbase_trim():
    objects = []
    options = "trim/10"

    req = requests.get(const.base_url + const.vehiclesbase + options)
    objects.append(req)

    assert 200 == req.status_code
    print(req.json())
    print(objects)

if __name__ == '__main__':
    test_get_vehiclesbase_makes()