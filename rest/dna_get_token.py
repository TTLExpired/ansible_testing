# A small script to automate getting a token from Cisco DNA
import requests
import json


def get_token(auth_url, username, password):
    '''
    A small script to get Token from Cisco DNA center.
    In general, token expires in about 10 minutes.

    Three things are required, and all hard coded:
        1. Autl URL
        2. Username
        3. Password
    All are provided in main function for easy change.
    '''
    token = requests.post(auth_url, auth=(username, password)).json()
    token = token['Token']

    return token


def main():
    '''
    This is the smallest main. Basically statics with token returned.
    '''
    # First, username and passwords
    username = 'devnetuser'
    password = 'Cisco123!'

    # Auth Base URL
    auth_url = 'https://sandboxdnac.cisco.com/api/system/v1/auth/token/'

    # Now get the token
    token = get_token(auth_url, username, password)
    headers = {'X-Auth-Token': token, 'Content-type': 'application/json'}

    print('Use this header: \n', headers)


if __name__ == '__main__':
    main()