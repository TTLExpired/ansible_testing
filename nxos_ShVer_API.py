# A test script to run 'sh ver' against Cisco Nexus API
# Import the needed libraries. JSON and Requests to process http/https payloads
import json
import requests
# Import Basic Auth from requests as we'll be passing creds
from requests.auth import HTTPBasicAuth

# Run the script directly
if __name__ == "__main__":

    # this is our basic authentication using requests basic module
    auth = HTTPBasicAuth('mossesb', 'password')
    # Also part of requests header. Standard stuff
    headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
            }
    # NX OS fixed URL.
    url = 'http://172.16.7.252/ins'

    # this is dictionary with 1 key 'ins_api' and 
    # Nested Value of further 6 key/value paris
    payload = {
      "ins_api": {
	"version": "1.0",
	"type": "cli_show",
	"chunk": "0",
	"sid": "1",
	"input": "sh version",
	"output_format": "json"
      }
    }

    # This is the main part. we're using the post function
    # within Request library.
    # First, we're doing a 'post'. It can also be 'GET' and so on.
    # Then we pass 4 objects to 'post'. URL, modulated in JSON the payload
    # the header and the authentication
    response = requests.post(url, data=json.dumps(payload),
			    headers=headers, auth=auth)
    
    # We now print the response. in this case, it's 200(OK)
    print(response)

    # Last, we modulate the response with Python and print
    # Sh version results
    print(response.text) 
