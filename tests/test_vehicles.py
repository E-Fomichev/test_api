import const
import requests
import json_data

"""Sammary"""

def test_get_vehicles_summary_show():
    """Получить информацию об авто"""

    objects = []
    headers = {'Authorization': const.auth}
    options = '/summary/'

    req = requests.get(const.base_url + const.vehicles + const.uid + options + const.vid,
                       headers=headers)
    objects.append(req)

    assert 200 == req.status_code
    print(req.json())
    print(objects)

"""SharedVehicle"""

def test_get_vehicles_sharedvehicle_index():
    """Список всех расшаренных авто для пользователя"""

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

def test_get_vehicles_sharedvehicle_show():
    """Информация о расшаренной машине"""

    objects = []
    headers = {'Authorization': const.auth}
    options = '/shared/'

    req = requests.get(const.base_url + const.vehicles + const.uid + options + const.shared_id,
                       headers=headers)
    objects.append(req)

    assert 200 == req.status_code
    print(req.json())
    print(objects)

# def test_del_vehicles_sharedvehicle_delete():
#     """Удаление расшаренной машины у пользователя"""

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

"""OwnVehicleRequest"""

def test_post_vehicles_own_request():
    """Отправка информации об авто на подтверждение"""

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

def test_get_vehicles_own_request():
    """Запрос информации по учетной записи авто"""

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

"""OdometerReading"""

def test_get_vehicles_own_odometr_show():
    """Отображаение пробега авто"""

    objects = []
    headers = {'Authorization': const.auth}
    options = '/own/'
    options_2 = '/odometer'

    req = requests.get(const.base_url + const.vehicles + const.uid + options + const.vid + options_2,
                        headers=headers)
    objects.append(req)

    assert 200 == req.status_code
    print(req.json())
    print(objects)

def test_post_vehicles_own_odometr_create():
    """Изменение пробега авто"""

    objects = []
    headers = {'Authorization': const.auth}
    options = '/own/'
    options_2 = '/odometer'
    json = json_data.json_odometer

    req = requests.post(const.base_url + const.vehicles + const.uid + options + const.vid + options_2,
                        headers=headers,
                        json=json)
    objects.append(req)

    assert 201 == req.status_code
    print(req.json())
    print(objects)

"""Drivers"""

def test_post_vehicles_own_drivers_create():
    """Добавление пользователя в расшаренные"""

    objects = []
    headers = {'Authorization': const.auth}
    options = '/own/'
    options_2 = '/drivers'
    json = json_data.json_shared_person

    req = requests.post(const.base_url + const.vehicles + const.uid + options + const.vid + options_2,
                        headers=headers,
                        json=json)
    objects.append(req)

    assert 201 == req.status_code
    print(req.json())
    print(objects)

def test_get_vehicles_own_drivers_index():
    """Отображаение расшаренных водителей для авто"""

    objects = []
    headers = {'Authorization': const.auth}
    options = '/own/'
    options_2 = '/drivers'

    req = requests.get(const.base_url + const.vehicles + const.uid + options + const.vid + options_2,
                        headers=headers)
    objects.append(req)

    assert 200 == req.status_code
    print(req.json())
    print(objects)

def test_del_vehicles_own_drivers_delete():
    """Удаление расшаренного водителя от авто"""

    objects = []
    headers = {'Authorization': const.auth}
    options = '/own/'
    options_2 = '/drivers/'

    req = requests.delete(const.base_url + const.vehicles + const.uid + options + const.vid + options_2 + const.shared_person_id,
                        headers=headers)
    objects.append(req)

    assert 200 == req.status_code
    print(req.json())
    print(objects)

"""OwnVehicle"""

def test_get_vehicles_own_controller_index():
    """Получение id всех авто по пользователю"""

    objects = []
    headers = {'Authorization': const.auth}
    params = {'include': 'all'}
    options = '/own'

    req = requests.get(const.base_url + const.vehicles + const.uid + options,
                        headers=headers,
                        params=params)
    objects.append(req)

    assert 200 == req.status_code
    print(req.json())
    print(objects)

def test_get_vehicles_own_controller_summary():
    """Получение всей инфы по автомобилям пользователя"""

    objects = []
    headers = {'Authorization': const.auth}
    params = {'include': 'all'}
    options = '/own/summary'

    req = requests.get(const.base_url + const.vehicles + const.uid + options,
                        headers=headers,
                        params=params)
    objects.append(req)

    assert 200 == req.status_code
    print(req.json())
    print(objects)

def test_get_vehicles_own_controller_show():
    """Получение информации по автомобилю пользователя"""

    objects = []
    headers = {'Authorization': const.auth}
    options = '/own/'

    req = requests.get(const.base_url + const.vehicles + const.uid + options + const.vid,
                        headers=headers)
    objects.append(req)

    assert 200 == req.status_code
    print(req.json())
    print(objects)

def test_post_vehicles_own_controller_create():
    """Отправить/отредактировать информацию об автомобиле"""

    objects = []
    headers = {'Authorization': const.auth}
    options = '/own/'
    json = json_data.json_auto_details

    req = requests.post(const.base_url + const.vehicles + const.uid + options + const.vid,
                        headers=headers,
                        json=json)
    objects.append(req)

    assert 201 == req.status_code
    print(req.json())
    print(objects)

# def test_del_vehicles_own_controller_delete():
#     """Удаление автомобиля из профиля"""
#
#     objects = []
#     headers = {'Authorization': const.auth}
#     options = '/own/'
#
#     req = requests.delete(const.base_url + const.vehicles + const.uid + options + const.vid,
#                         headers=headers)
#     objects.append(req)
#
#     assert 200 == req.status_code
#     print(req.json())
#     print(objects)

"""Reviewer"""

def test_get_vehicles_reviewer_index():
    """Получение списка пользователей с авто по статусам submitted, prepared, accepted, rejected, assembling """

    objects = []
    headers = {'Authorization': const.auth}
    params = {'limit': '20', 'status': 'submitted', 'offset': '0'}
    options = 'requests'

    req = requests.get(const.base_url + const.vehicles + options,
                        headers=headers,
                        params=params)
    objects.append(req)

    assert 200 == req.status_code
    print(req.json())
    print(objects)

def test_get_vehicles_reviewer_count():
    """Получение количества пользователей по статусам submitted, prepared, accepted, rejected, assembling """

    objects = []
    headers = {'Authorization': const.auth}
    params = {'status': 'submitted'}
    options = 'requests/count'

    req = requests.get(const.base_url + const.vehicles + options,
                        headers=headers,
                        params=params)
    objects.append(req)

    assert 200 == req.status_code
    print(req.json())
    print(objects)

def test_post_vehicles_reviewer_reject():
    """Отклонение заявки автомобиля"""

    objects = []
    headers = {'Authorization': const.auth}
    options = 'requests/'
    options_2 = '/reject'
    json = json_data.json_reject_car

    req = requests.post(const.base_url + const.vehicles + options + const.vid + options_2,
                        headers=headers,
                        json=json)
    objects.append(req)

    assert 201 == req.status_code
    print(req.json())
    print(objects)

def test_post_vehicles_reviewer_prepare():
    """Подготовка заявки автомобиля"""

    objects = []
    headers = {'Authorization': const.auth}
    options = 'requests/'
    options_2 = '/prepare'
    json = json_data.json_prepare_car

    req = requests.post(const.base_url + const.vehicles + options + const.vid + options_2,
                        headers=headers,
                        json=json)
    objects.append(req)

    assert 201 == req.status_code
    print(req.json())
    print(objects)

def test_post_vehicles_reviewer_accept_prepared():
    """Подтверждение заявки автомобиля"""

    objects = []
    headers = {'Authorization': const.auth}
    options = 'requests/'
    options_2 = '/accept_prepared'

    req = requests.post(const.base_url + const.vehicles + options + const.vid + options_2,
                        headers=headers)
    objects.append(req)

    assert 201 == req.status_code
    print(req.json())
    print(objects)

def test_post_vehicles_reviewer_accept():
    """Подтверждение заявки автомобиля"""

    objects = []
    headers = {'Authorization': const.auth}
    options = 'requests/'
    options_2 = '/accept'
    json = json_data.json_accept_car

    req = requests.post(const.base_url + const.vehicles + options + const.vid + options_2,
                        headers=headers,
                        json=json)
    objects.append(req)

    assert 201 == req.status_code
    print(req.json())
    print(objects)

if __name__ == '__main__':
    test_get_vehicles_summary_show()