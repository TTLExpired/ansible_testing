# Python and Restconf to a CSR
import json
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":

    # Standard header from Request Method with formatting as Yang and Json
    auth = HTTPBasicAuth('mossesb', 'password')
    headers = {
            'Accept': 'application/vnd.yang.data+json',
            'Content-Type': 'application/vnd.yang.data+json'
            }

    # the device we're working on
    url = 'http://172.16.7.251/restconf/api/config/native?deep'
    # Formulating and sending the API call, with data modulationg type and auth
    response = requests.get(url, headers=headers, auth=auth)

    # We assign the respone to variable response
    response= json.loads(response.text)
    # We now print according to json formatting and adding indent of 4
    print(json.dumps(response, indent=4))
