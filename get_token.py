import argparse
import subprocess
import requests
import json
import base64
from jose import jwt
from warrant import Cognito

# parser = argparse.ArgumentParser()
# parser.add_argument('-u', '--username', help='Cognito user name')
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


def ping_ip():
    # '''
    # Ping IP address and return tuple:
    # On success: (return code = 0, command output)
    # On failure: (return code, error output (stderr))
    # '''
    # reply = subprocess.run('ping -c {count} -n {ip}'
    #                        .format(count=count, ip=ip_address),
    #                        shell=True,
    #                        stdout=subprocess.PIPE,
    #                        stderr=subprocess.PIPE,
    #                        encoding='utf-8')
    # if reply.returncode == 0:
    #     return True, reply.stdout
    # else:
    #     return False, reply.stdout+reply.stderr



    parser = argparse.ArgumentParser(description='Ping script')

    parser.add_argument('-u', '+79000000001', help='Cognito user name')
    parser.add_argument('-p', 'Password_1122', help='Cognito user password')
    parser.add_argument('--stage', 'fd-dev', help='Stage: fd-dev')

    args = parser.parse_args()
    print(args)

    # rc, message = ping_ip(args.ip, args.count)
    # print(message)

if __name__ == '__main__':
    ping_ip()