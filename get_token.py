# python get_token.py -u +79000000001 -p Password_1122 --stage fd-dev
# import argparse
# import requests
# import json
# import base64
# from jose import jwt
# from warrant import Cognito
#
# parser = argparse.ArgumentParser()
# parser.add_argument('-u', '--username', help='+79000000001')
# parser.add_argument('-p', '--password', help='Cognito user password')
# parser.add_argument('--stage', required=True, help='Stage: fd-dev')
# args = parser.parse_args()
# pools = {
#     'fd-dev': ('5lsc77b9b4kiu6mo80pndmt4if', 'eu-central-1_ZlwxZj0BA')
# }
# client_id, user_pool = pools[args.stage]
#
# user = Cognito(user_pool, client_id,
#                username=args.username,
#                #access_key = 'fake',
#                #secret_key = 'deep_fake',
#                user_pool_region='eu-central-1')
# user.authenticate(args.password)
# token = user.id_token
# print(token)

import argparse
import requests
import json
import base64
from jose import jwt
from warrant import Cognito
#parser = argparse.ArgumentParser()
#parser.add_argument('-u', '--username', help='Cognito user name')
#parser.add_argument('-p', '--password', help='Cognito user password')
#parser.add_argument('--stage', required=True, help='Stage: fd-dev')
#args = parser.parse_args()
pools = {
    'fd-dev': ('5lsc77b9b4kiu6mo80pndmt4if', 'eu-central-1_ZlwxZj0BA')
}
client_id, user_pool = pools['fd-dev']
user = Cognito(user_pool, client_id,
               username='+79000000001',
               # access_key = 'fake',
               # secret_key = 'deep_fake',
               user_pool_region='eu-central-1')
user.authenticate('Password_1122')
token = user.id_token
print(token)
