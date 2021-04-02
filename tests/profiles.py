import requests
import const
import json_data


"""Confirmation"""
def test_post_profiles_confirmation_create():
    """Регистрация пользователя в системе"""

    objects = []
    headers = {'Authorization': const.token}
    options = 'confirmation'
    json = json_data.json_confirmation

    req = requests.post(const.base_url + const.profiles + options,
                        headers=headers,
                        json=json)
    objects.append(req)

    assert 201 == req.status_code
    print(req.json())
    print(objects)

"""Details"""
def test_get_profiles_details_list():
    """Получение выборки по аккаунтам через continuation, limit"""

    objects = []
    headers = {'Authorization': const.token}
    params = {'continuation': '10', 'limit': '10'}
    options = 'profile'

    req = requests.get(const.base_url + const.profiles + options,
                        headers=headers,
                        params=params)
    objects.append(req)

    assert 200 == req.status_code
    print(req.json())
    print(objects)

def test_get_profiles_details_get():
    """Получение данных о профиле"""

    objects = []
    headers = {'Authorization': const.token}
    options = '/profile/details'

    req = requests.get(const.base_url + const.profiles + const.uid + options,
                        headers=headers)
    objects.append(req)

    assert 200 == req.status_code
    print(req.json())
    print(objects)

def test_post_profiles_details_picture_load():
    """Загрузка аватара"""

    objects = []
    headers = {'Authorization': const.token}
    options = '/profile/picture'
    json = json_data.json_picture_load

    req = requests.post(const.base_url + const.profiles + const.uid + options,
                        headers=headers,
                        json=json)
    objects.append(req)

    assert 201 == req.status_code
    print(req.json())
    print(objects)




