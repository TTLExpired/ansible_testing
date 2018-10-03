import json
import requests

# First example script to pulling data of Cisco Always on DNA service.

def get_auth_token(auth_url, username, password):
    '''
    A function to get token.
    1 - Get the URL from MAIN
    2 - Use the username and password given by Cisco Always on Labs
    3 - Return Token, strip the dictionary and send value.
    '''
    token = requests.post(auth_url, auth=(username, password)).json()

    # Return just the token. Fuck dictionary
    return token['Token']


def get_net_devices(devices_url, headers):
    '''
    A function to return list of network devices.
    Very specific. However, it has a couple of things:
    1 - Headers - A constant to use in Requests libary.
    2 - Format in JSON.

    Return Value
    '''
    devices = requests.get(devices_url, headers=headers).json()
    # Return Device Data
    return devices


def main():
    '''
    A simple Script to fitch some info from Cisco Always on DNA labs.
    We need few variables:
        Cisco_URL = sandboxdnac.cisco.com
        Rest_URL = api/v1
        Auth_URL = auth/token

    Once we get the token, we're able to start pulling some info.
    in this case, we'll be using network-devices.

    Please note this ex1. There will be more examples of this shit as
    we go along.

    Please note the difference between AUTH URL and network-device URL!!!
    '''
    # Let's start with basic defs
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

    # network-devices URL
    devices_url = cisco_url + get_url + devices_url

    # Lets get the token
    token = get_auth_token(auth_url, username, password)

    # Now that we have the token, lets setup requests header
    headers = {'X-Auth-Token': token,
               'Content-type': 'application/json'}

    # Now that we have the headers, lets pull some devices info
    network_devices = get_net_devices(devices_url, headers)

    # Let's print it for testing.
    print(json.dumps(network_devices, indent=2))


if __name__ == '__main__':
    main()