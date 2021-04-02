from warrant import Cognito
# python get_token.py -u +79000000001 -p Password_1122 --stage fd-dev
# python get_last_trip.py 2000041061 61778 979151


pools = {
    'fd-dev': ('5lsc77b9b4kiu6mo80pndmt4if', 'eu-central-1_ZlwxZj0BA')
}
client_id, user_pool = pools['fd-dev']
user = Cognito(user_pool, client_id,
               username='+79000000001',
               user_pool_region='eu-central-1')
user.authenticate('Password_1122')
token = user.id_token


base_url = 'https://fd19-trial.sredasolutions.com/'
vehiclesbase = 'vehicles-base/v0/'
stables = 'stables/v0/'
poffers = 'poffers/v0/'
pdfmaker = 'pdf/v0/policy/'
vehicles = 'vehicles/v0/'
modellier = 'modellier/v0/'
profiles = 'profiles/v0/'


phone_number = '+79819519527' #+79531495436
uid = '2000042120'   #2000041833
vid = 'cb2a18b7cb9e123c078ca092397ecd085e5b7d8173fd7a1377d7bf3ea98236ce'  #127bbc79ff98b7091d97e7a3f3daa9a732e966e18e55403793ab130aa0b5e1fe
shared_id = '3928936fe295d6b5e4abf64ea01b9f67f48d982cf5c4a46db9c91374a1e97c34'
shared_person = 2000041833
shared_person_id = '2000041833'
parking_id = '61793'
trip_id = '61787'
model_id = '1'
response_id = '758'
driver_licence = '6415121021'