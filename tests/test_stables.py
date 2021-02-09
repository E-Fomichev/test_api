import requests
import const
import time
import json_data

"""Search"""

def test_get_stables_plate():
    """Найти информацию по госзнаку автомобиля"""

    objects = []
    number = 'Н504АР799'
    options = 'plates/ru/'
    headers = {'Authorization': const.auth}

    req = requests.get(const.base_url + const.stables + options + number,
                       headers=headers)
    objects.append(req)
    req.json()
    time.sleep(5)
    req = requests.get(const.base_url + const.stables + options + number,
                       headers=headers)

    assert 200 == req.status_code
    print(req.json())
    print(objects)

def test_get_stables_vin():
    """Найти информацию по vin номеру автомобиля"""

    objects = []
    vin = 'WBANA71030B605898'
    options = 'vin/'
    headers = {'Authorization': const.auth}

    req = requests.get(const.base_url + const.stables + options + vin,
                       headers=headers)
    objects.append(req)
    req.json()
    time.sleep(5)
    req = requests.get(const.base_url + const.stables + options + vin,
                       headers=headers)

    assert 200 == req.status_code
    print(req.json())
    print(objects)

"""Report"""

def test_post_stables_report_criminal():
    """Отчет по розыску"""

    objects = []
    options = 'report/wanted_criminal'
    headers = {'Authorization': const.auth}
    json = json_data.json_wanted_criminal

    req = requests.post(const.base_url + const.stables + options,
                        headers=headers,
                        json=json)
    objects.append(req)
    req.json()
    time.sleep(2)
    req = requests.post(const.base_url + const.stables + options,
                        headers=headers,
                        json=json)

    assert 200 == req.status_code
    print(req.json())
    print(objects)

def test_post_stables_tickets():
    """Создает отчет о штрафах по ву"""

    objects = []
    options = 'report/tickets'
    headers = {'Authorization': const.auth}
    json = json_data.json_licence

    req = requests.post(const.base_url + const.stables + options,
                        headers=headers,
                        json=json)
    objects.append(req)
    req.json()
    time.sleep(3)
    req = requests.post(const.base_url + const.stables + options,
                        headers=headers,
                        json=json)

    assert 200 == req.status_code
    print(req.json())
    print(objects)

def test_post_stables_ownership():
    """Создает отчет об автомобилях, которыми владел собственник"""

    objects = []
    options = 'report/ownership'
    headers = {'Authorization': const.auth}
    json = json_data.json_ownership

    req = requests.post(const.base_url + const.stables + options,
                        headers=headers,
                        json=json)
    objects.append(req)
    req.json()
    time.sleep(5)
    req = requests.post(const.base_url + const.stables + options,
                        headers=headers,
                        json=json)

    assert 200 == req.status_code
    print(req.json())
    print(objects)

# def test_post_stables_migration():   # нет данных json, платный запрос, у Артема нет особой инфы по нему
#     """Создает отчет ///"""
#
#     objects = []
#     options = 'report/migration_compliance'
#     headers = {'Authorization': const.auth}
#     json = json_data.json_migration
#
#     req = requests.post(const.base_url + const.stables + options,
#                         headers=headers,
#                         json=json)
#     objects.append(req)
#     req.json()
#     time.sleep(5)
#     req = requests.post(const.base_url + const.stables + options,
#                         headers=headers,
#                         json=json)
#
#     assert 200 == req.status_code
#     print(req.json())
#     print(objects)

def test_post_stables_blacklist():   # нет данных json
    """Проверка по черному списку"""

    objects = []
    options = 'report/blacklist'
    headers = {'Authorization': const.auth}
    json = json_data.json_blacklist

    req = requests.post(const.base_url + const.stables + options,
                        headers=headers,
                        json=json)
    objects.append(req)
    req.json()
    time.sleep(5)
    req = requests.post(const.base_url + const.stables + options,
                        headers=headers,
                        json=json)

    assert 200 == req.status_code
    print(req.json())
    print(objects)


if __name__ == '__main__':
    test_get_stables_plate()