import requests
import openpyxl
import csv

auth = 'eyJraWQiOiIzM3dZZHJmNFUyM1dtak8yVzlySE91NFlHV2QrNEVFV0ZFbHQ1UUw0NVdrPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiIzYzc0OWU1MS00MmQzLTQwZDItYTllOS00YWEwMTYwNjJmMjIiLCJhdWQiOiI1bHNjNzdiOWI0a2l1Nm1vODBwbmRtdDRpZiIsImNvZ25pdG86Z3JvdXBzIjpbImFkbWlucyJdLCJldmVudF9pZCI6IjdjNTkyOTM2LTg3MjktNDNkMS05YmMyLWM5OTkzYjA3YmE2NSIsInRva2VuX3VzZSI6ImlkIiwiYXV0aF90aW1lIjoxNjEzNDkwNTYwLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuZXUtY2VudHJhbC0xLmFtYXpvbmF3cy5jb21cL2V1LWNlbnRyYWwtMV9abHd4WmowQkEiLCJjdXN0b206dWlkIjoiMjAwMDAwMjgxNiIsImNvZ25pdG86dXNlcm5hbWUiOiIzYzc0OWU1MS00MmQzLTQwZDItYTllOS00YWEwMTYwNjJmMjIiLCJleHAiOjE2MTM0OTQxNjAsImlhdCI6MTYxMzQ5MDU2MH0.GzquuF-4kaC9W913Da7KH4S8zlAWtIAU-YIu2LMBavtEnf8EY9ehpai42K17wii13WMHgyZ6PG-L5baUww7BsU2b2houWhTv7GWOuXsKBvtRqCTUdzgkMxx8Hppgoo3sJeZSyI1WNTbmMXawxrsHh6Lgz21KuvKBcaFiFVwaFL3gclIZXkrDB3xnOcdqIvzjJLQKGYwj7wEvMq0-BUPEA5Qa7E91KfTlwJ1J_RduJ9UId_8HYT64Tj5WIDSUEeVjW72w1vjD-pF01mVSY3bCfSuEPK-MCmsqMZTqTX-ljOI1ViGbJl9N_81Fq0eUOkfXDPnlwDGr_DcJzveOb882hg'
vid = 'ef09ab94cb5b4afc3ba71240fc5a5317eb1c844725fa03b3d4e9e44a7278660c'
uid = '2000042120'
base_url = 'https://fd19-trial.sredasolutions.com/'
poffers = 'poffers/v0/'
vehicles = 'vehicles/v0/'

# mark =  ('Audi')
# models = ('A1', 'A3')
years = (2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014) #  (2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013)
# sum_ins = ('1695100', '1695100', '1695100', '1864610')

time = ['2021', '2020', '2019', '2018', '2017', '2016', '2015', '2014']


def test_calc_tarif():
    with open('price.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")
        for row in reader:
            mark = row["Mark"]
            model = row["model"]
            # for god in time:

            for year in years:

                a = row[time]
                json = {
                    "year": year,
                    "plate": {
                        "value": "в666ор77",
                        "type": "russia93"
                    },
                    "model": model,
                    "make": mark}
                objects = []
                headers = {'Authorization': auth}
                options = '/own/'

                req = requests.post(base_url + vehicles + uid + options + vid,
                                   headers=headers,
                                   json=json)
                objects.append(req)

                assert 201 == req.status_code
                objects = []
                dop_url = 'parking'
                params = {'vid': vid, 'lifetime': '60', 'type': 'garage', 'lat': '11.1', 'lon': '12.2'}
                headers = {'Authorization': auth}

                req = requests.get(base_url + poffers + uid + '/' + dop_url,
                                   headers=headers,
                                   params=params)
                objects.append(req)

                data = req.json()

                if 200 == req.status_code:
                    print(mark, model, year, a, data[0]['policy']['coverage']['damage']['value'])
                else:
                    print(mark, model, year, req.status_code)



# def test_load_full_tarifficator():
#
#     price_book = openpyxl.open('Price_Book.xlsx', data_only=True)
#     sheet = price_book.active
#     cells = sheet['A30':'B40']
#     for mark, model in cells:
#         print(mark.value, model.value)


# def test_calc_tarif():
#     with open('price.csv', newline='') as csvfile:
#         reader = csv.DictReader(csvfile, delimiter=",")
#         for row in reader:
#             mark = row["Mark"]
#             model = row["model"]
#             for year in years:
#                 json = {
#                     "year": year,
#                     "plate": {
#                         "value": "в666ор77",
#                         "type": "russia93"
#                     },
#                     "model": model,
#                     "make": mark}
#                 objects = []
#                 headers = {'Authorization': auth}
#                 options = '/own/'
#
#                 req = requests.post(base_url + vehicles + uid + options + vid,
#                                    headers=headers,
#                                    json=json)
#                 objects.append(req)
#
#                 assert 201 == req.status_code
#                 objects = []
#                 dop_url = 'parking'
#                 params = {'vid': vid, 'lifetime': '60', 'type': 'garage', 'lat': '11.1', 'lon': '12.2'}
#                 headers = {'Authorization': auth}
#
#                 req = requests.get(base_url + poffers + uid + '/' + dop_url,
#                                    headers=headers,
#                                    params=params)
#                 objects.append(req)
#
#                 print(mark, model, year, req.json())


# def test_calc_tarif():
#     for model in models:
#         for year in years:
#             json = {
#                 "year": year,
#                 "plate": {
#                     "value": "в666ор77",
#                     "type": "russia93"
#                 },
#                 "model": model,
#                 "make": mark}
#             objects = []
#             headers = {'Authorization': auth}
#             options = '/own/'
#
#             req = requests.post(base_url + vehicles + uid + options + vid,
#                                 headers=headers,
#                                 json=json)
#             objects.append(req)
#
#             assert 201 == req.status_code
#             objects = []
#             dop_url = 'parking'
#             params = {'vid': vid, 'lifetime': '60', 'type': 'garage', 'lat': '11.1', 'lon': '12.2'}
#             headers = {'Authorization': auth}
#
#             req = requests.get(base_url + poffers + uid + '/' + dop_url,
#                                headers=headers,
#                                params=params)
#             objects.append(req)
#             data = req.json()
#
#             if 200 == req.status_code and data[0]['policy']['coverage']['damage']['value'] == sum_ins:
#                 print(mark, model, year, data[0]['policy']['coverage']['damage']['value'])
#             elif 200 == req.status_code and data[0]['policy']['coverage']['damage']['value'] != sum_ins:
#                 print(mark, model, year, 'error insured sum')
#             else:
#                 print(mark, model, year, req.status_code)