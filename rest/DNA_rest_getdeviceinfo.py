import requests
import json
from cisco_dna_ex1 import get_auth_token

# A sample Script to get specific Device Info


def main():
    '''
    A script to get device Info.
    First, pull the function get_auth_info from cisco_dna_ex1 for token.
    then do something with it.
    To be explained fully
    '''

    cisco_url = 'https://sandboxdnac.cisco.com/'
    rest_url = 'api/system/v1/'
    get_url = 'api/v1/'
    auth_url = 'auth/token/'
    devices_url = 'network-device'

    # User Creds
    username = 'devnetuser'
    password = 'Cisco123!'

    # Easy, Auth Token URL
    auth_url = cisco_url + rest_url + auth_url

    token = get_auth_token(auth_url, username, password)

    # Now that we have the token, lets setup requests header
    headers = {'X-Auth-Token': token,
               'Content-type': 'application/json'}

    print(token)


if __name__ == '__main__':
    main()