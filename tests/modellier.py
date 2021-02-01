import requests
import const
import json_data

def test_get_modellier_report_latest():
    objects = []
    headers = {'Authorization': const.auth}
    options = '/report/'
    options_2 = '/latest'

    req = requests.get(const.base_url + const.modellier + const.uid + options + const.trip_id + options_2,
                           headers=headers)
    objects.append(req)

    assert 200 == req.status_code
    print(req.json())
    print(objects)

def test_get_modellier_report_list():
    objects = []
    headers = {'Authorization': const.auth}
    options = '/report/'

    req = requests.get(const.base_url + const.modellier + const.uid + options + const.trip_id,
                           headers=headers)
    objects.append(req)

    assert 200 == req.status_code
    print(req.json())
    print(objects)


def test_get_modellier_analytics_index():
    objects = []
    options = '/model/'
    options_2 = '/response'
    params = {'trip_id': const.trip_id}
    headers = {'Authorization': const.auth}

    req = requests.get(const.base_url + const.modellier + const.uid + options + const.model_id + options_2,
                       headers=headers,
                       params=params)
    objects.append(req)
    req.json()

    assert 200 == req.status_code
    print(req.json())
    print(objects)

# def test_post_modellier_analytics_create():
#     objects = []
#     options = '/model/'
#     options_2 = '/response'
#     headers = {'Authorization': const.auth}
#
#     json = json_data.json_report
#     req = requests.post(const.base_url + const.modellier + const.uid + options + const.model_id + options_2,
#                        headers=headers,
#                        json=json)
#     objects.append(req)
#     req.json()
#
#     assert 200 == req.status_code
#     print(req.json())
#     print(objects)

def test_get_modellier_analytics_show():
    objects = []
    headers = {'Authorization': const.auth}
    options = '/model/'
    options_2 = '/response/'

    req = requests.get(const.base_url + const.modellier + const.uid + options + const.model_id + options_2 + const.response_id,
                       headers=headers)
    objects.append(req)

    assert 200 == req.status_code
    print(req.json())
    print(objects)

# def test_del_modellier_analytics_delete():
#     objects = []
#     headers = {'Authorization': const.auth}
#     options = '/model/'
#     options_2 = '/response/'
#
#     req = requests.delete(const.base_url + const.modellier + const.uid + options + const.model_id + options_2 + const.response_id,
#                        headers=headers)
#     objects.append(req)
#
#     assert 200 == req.status_code
#     print(req.json())
#     print(objects)

# Удаление отчетов


def test_get_modellier_controller_index(): # Отображение списка моделей
    objects = []
    headers = {'Authorization': const.auth}
    options = '/model/'

    req = requests.get(const.base_url + const.modellier + const.uid + options,
                       headers=headers)
    objects.append(req)

    assert 200 == req.status_code
    print(req.json())
    print(objects)

def test_post_modellier_controller_create(): # Создание модели
    objects = []
    headers = {'Authorization': const.auth}
    options = '/model/'
    json = json_data.json_create_car

    req = requests.post(const.base_url + const.modellier + const.uid + options,
                       headers=headers,
                       json=json)
    objects.append(req)

    assert 200 == req.status_code
    print(req.json())
    print(objects)

# def test_post_modellier_controller_delete(): # Удаление модели
#     objects = []
#     headers = {'Authorization': const.auth}
#     options = '/model/'
#
#     req = requests.post(const.base_url + const.modellier + const.uid + options + 'id', # id из теста выше test_post_modellier_controller_create
#                        headers=headers)
#     objects.append(req)
#
#     assert 200 == req.status_code
#     print(req.json())
#     print(objects)


