import const


json_ride = {
    "vehicle_id": const.vid,
    "points": [
        {
            "lon": "30.285109",
            "lat": "59.8151394"
        },
        {
            "lon": "37.5570742",
            "lat": "55.7676586"
        },
        {
            "lon": "33.5274371",
            "lat": "58.1904624"
        }
    ]
}

json_car = {
    "make": "Audi",
    "model": "A1",
    "age": 1
}

json_odometr = {
    "mileage_unit": 100,
    "mileage_value": "miles",
    "image": {
        "collection": "ea sunt commodo",
        "key": "veniam in aliquip incididunt"
    }
}

json_report = {
    "composite_report_id": "<integer>",
    "result": "<object>",
    "trip_id": "<integer>",
    "model_id": "<integer>",
    "id": "<integer>"
}

json_create_car = {
    "name": "4 серия",
    "id": 19775,
    "description": "4 серия"
}

json_update_car = {
    "name": "4 серия",
    "id": 19775,
    "description": "Четвертая серия"
}

json_wanted_criminal = {
    "birth": "01.01.2002",
    "last_name": "cupidatat culpa in",
    "first_name": "ea sunt officia voluptate in",
    "patronymic": "sit enim laboris eu dolor"
}

json_licence = {
    "driver_licence": const.driver_licence
}

json_ownership = {
    "birth": "02.04.1989",
    "last_name": "Фомичев",
    "first_name": "Евгений",
    "patronymic": "Геннадьевич",
    "passport": "6308 301390",
    "driver_licence": "6415121021"
}

json_migration = {
    "street": "ex amet in",
    "city": "Ut sunt do",
    "passport_date": "01.01.2000",
    "passport": "1234 123412",
    "house": "e",
    "district": "amet ea sint",
    "corps": "mollit quis anim",
    "apartment": "sit sunt tempor dolor elit"
}

json_blacklist = {
    "birth": "01.01.2000",
    "last_name": "mollit non id sit",
    "first_name": "anim",
    "street": "incididunt id Ut",
    "phone": "nostrud dolore culpa officia",
    "patronymic": "dolor veniam officia ad",
    "passport": "1234 123412",
    "isTemporalAddress": True,
    "inn": 47825415,
    "house": "do dolore veniam",
    "corps": "cupidatat veniam laborum proident",
    "city": "ut aute",
    "building": "do adipisicing velit in",
    "apartment": "eiusmod ut magna eni"
}

json_shared_person = {
    "comment": "magna cillum id mollit",
    "uid": const.shared_person
}

json_odometer = {
    "mileage_unit": "km",
    "mileage_value": 10001,
    "image": {
        "collection": "do labore esse",
        "key": "exercitation nulla nostrud"
    }
}

json_auto_details = {
    "year": 2014,
    "plate": {
        "value": "в666ор77",
        "type": "russia93"
    },
    "model": "Kalina",
    "make": "Lada"
}

json_reject_car = {
    "reason": "malformed",
    "comment": "reprehenderit sed mollit dolor"
}

json_prepare_car = {
  "type": "russia2020-08-26",
  "recognized": {
    "registration": {
      "vin": "sdfdsf405645604",
      "registration_number": "р618тр178",
      "engine_volume": 1799,
      "engine_power": 125
    },
    "plate": {
      "value": "1231456456",
      "type": "russia93"
    }
  },
  "comment": "string",
  "source": "manual"
}

json_accept_car = {
  "type": "russia2019",
  "recognized": {
    "registration": {
      "vin": "dfgdfgdfg6504560456",
      "registration_number": "р618тр178",
      "engine_volume": 1200,
      "engine_power": 110
    },
    "plate": {
      "value": "string",
      "type": "russia93"
    }
  },
  "comment": "string"
}

json_confirmation = {
    "username": "0db1cf9a-5b86-4f9f-a062-0cf1ec823990"
}

json_picture_load = {
    "collection": "fugiat aliquip in commodo",
    "key": "laborum officia proident consectetur"
}