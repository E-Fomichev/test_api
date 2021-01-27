import requests
import const
import time


def test_get_stables():
    objects = []
    number = ("Н504АР799")
    headers = {'Authorization': const.auth}

    req = requests.get(const.base_url + const.stables + number, headers=headers)
    objects.append(req)
    req.json()
    time.sleep(5)
    req = requests.get(const.base_url + const.stables + number, headers=headers)

    assert 200 == req.status_code
    print(req.json())
    print(objects)

if __name__ == '__main__':
    test_get_stables()