import requests
import csv
from warrant import Cognito

vid = 'ef09ab94cb5b4afc3ba71240fc5a5317eb1c844725fa03b3d4e9e44a7278660c'
uid = '2000042120'
base_url = 'https://fd19-trial.sredasolutions.com/'
poffers = 'poffers/v0/'
vehicles = 'vehicles/v0/'

pools = {
    'fd-dev': ('5lsc77b9b4kiu6mo80pndmt4if', 'eu-central-1_ZlwxZj0BA')
}
client_id, user_pool = pools['fd-dev']
user = Cognito(user_pool, client_id,
               username='+79000000001',
               user_pool_region='eu-central-1')
user.authenticate('Password_1122')
token = user.id_token


years = ['2021', '2020', '2019', '2018', '2017', '2016', '2015', '2014']


def test_calc_tarif():
    with open('price.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")
        for row in reader:
            mark = row["Mark"]
            model = row["model"]


            for year in years:

                year = int(year)
                json = {
                    "year": year,
                    "plate": {
                        "value": "в666ор77",
                        "type": "russia93"
                    },
                    "model": model,
                    "make": mark}

                objects = []
                headers = {'Authorization': token}
                options = '/own/'

                req = requests.post(base_url + vehicles + uid + options + vid,
                                   headers=headers,
                                   json=json)
                objects.append(req)

                assert 201 == req.status_code
                objects = []
                dop_url = 'parking'
                params = {'vid': vid, 'lifetime': '60', 'type': 'garage', 'lat': '11.1', 'lon': '12.2'}
                headers = {'Authorization': token}

                req = requests.get(base_url + poffers + uid + '/' + dop_url,
                                   headers=headers,
                                   params=params)
                objects.append(req)

                data = req.json()
                year = str(year)
                a = row[year]
                a = a.replace(',','')

                if 200 == req.status_code and a == str(data[0]['policy']['coverage']['damage']['value']):
                    print(mark, model, year, 'Страховые суммы сходятся')
                elif 200 == req.status_code and a != str(data[0]['policy']['coverage']['damage']['value']):
                    print(mark, model, year,a, data[0]['policy']['coverage']['damage']['value'], 'Страховые суммы не сходятся')
                else:
                    print(mark, model, year, req.status_code, data['error'])



