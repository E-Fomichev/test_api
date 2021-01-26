import const
import requests


def test_get_pdfmaker():
    objects = []
    headers = {'Authorization': const.auth}

    req = requests.get(const.base_url + const.pdfmaker + const.uid + '/' + const.parking_id, headers=headers)
    objects.append(req)

    assert 200 == req.status_code
    print(objects)