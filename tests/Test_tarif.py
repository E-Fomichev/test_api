import requests
import openpyxl
import csv

auth = 'eyJraWQiOiIzM3dZZHJmNFUyM1dtak8yVzlySE91NFlHV2QrNEVFV0ZFbHQ1UUw0NVdrPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiIzYzc0OWU1MS00MmQzLTQwZDItYTllOS00YWEwMTYwNjJmMjIiLCJhdWQiOiI1bHNjNzdiOWI0a2l1Nm1vODBwbmRtdDRpZiIsImNvZ25pdG86Z3JvdXBzIjpbImFkbWlucyJdLCJldmVudF9pZCI6ImFiMGIwOWEzLTAxOWQtNDU5Yy1hMTczLWZiZDRmZmU3N2Q4YiIsInRva2VuX3VzZSI6ImlkIiwiYXV0aF90aW1lIjoxNjEzNDA5MTI5LCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuZXUtY2VudHJhbC0xLmFtYXpvbmF3cy5jb21cL2V1LWNlbnRyYWwtMV9abHd4WmowQkEiLCJjdXN0b206dWlkIjoiMjAwMDAwMjgxNiIsImNvZ25pdG86dXNlcm5hbWUiOiIzYzc0OWU1MS00MmQzLTQwZDItYTllOS00YWEwMTYwNjJmMjIiLCJleHAiOjE2MTM0MTI3MjksImlhdCI6MTYxMzQwOTEyOX0.H54eKtw4pS_-gzvp1sXN7XfPiF_xmu3_hofDqL9r-f7OZk_1dcsaQiLNun7ksnfiVlAMhkvkaU56UHRFsjuj380gfCQF7qSlXJqkviHtZK3kEoQUskXC6HNBDscZ0jmivqEIZEd9RirYDsMAUhOcQYLen-oCtncfAbFeSHwFqGBQmGSHaI-1mWd38ngIuTz5mX1UvBxlR-YKbNsE-ERjMExiWhAxEVBz-T9M1hDZB5QeSrIJMLbUd5fV_is2T_eNPyRod36qVAEGnReiBNoN8VWNWp3MHznfxnMMJyi6w8yjOFe239iNlBXhNaxmd2cyjKrvPZnWeuuCnznueJ5GQg'
vid = '67b611f0527b8dccab6d4ea051133e20795b3000092a52f92d8ab5aaba244fc5'
uid = '2000042120'
base_url = 'https://fd19-trial.sredasolutions.com/'
poffers = 'poffers/v0/'
vehicles = 'vehicles/v0/'


years = (2020, 2021) #  (2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013)

def test_calc_tarif():
    with open('price.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")
        for row in reader:
            mark = row["Mark"]
            model = row["model"]
            for year in years:
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

                print(mark, model, year, req.json())


# def test_load_full_tarifficator():
#
#     price_book = openpyxl.open('Price_Book.xlsx', data_only=True)
#     sheet = price_book.active
#     cells = sheet['A30':'B40']
#     for mark, model in cells:
#         print(mark.value, model.value)