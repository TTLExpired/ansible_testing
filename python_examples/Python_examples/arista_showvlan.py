# A python/JSON script for Arista
import json
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":

    auth = HTTPBasicAuth('mossesb', 'password')

    url = 'http://10.0.7.254/command-api'

    payload = {
      "jsonrpc": "2.0",
      "method": "runCmds",
      "params": {
	"format": "json",
	"timestamps": False,
	"autoComplete": False,
	"expandAliases": False,
	"cmds": [
	  "sh vlan brief"
	],
	"version": 1
      },
      "id": "EapiExplorer-1"
    }
    
    response = requests.post(url, data=json.dumps(payload), auth=auth)
    print('Status CODE: ' + str(response.status_code))

    print('RESPONSE:')
    results = json.loads(response.text)
    print(json.dumps(results, indent=4))
