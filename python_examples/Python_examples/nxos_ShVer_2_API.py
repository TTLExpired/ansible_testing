# Another NX OS python script.
import json
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":

    auth = HTTPBasicAuth('mossesb', 'password')

    url = 'http://172.16.7.252/ins'
    
    # Take extra arguments from command line. The first (1)
    # with the file name as (0) is to be assigned to variable command
    command = sys.argv[1]

    # If there's more than 2 arguments passed to the script:
    if len(sys.argv) > 2:
        # Assign command_type to the third string
        command_type = sys.argv[2]
    # Otherwise, use 'CLI_SHOW' as type
    else:
        command_type = 'cli_show'

    payload = {
            "ins_api": {
                "version": "1.0",
                # That's assigned from sys.argv
                "type": command_type,
                "chunk": "0",
                "sid": "1",
                # That's also assigned from the 'second' string passed to the string
                "input": command,
                "output_format": "json"
                }
            }

    # Our standard post method
    response = requests.post(url, data=json.dumps(payload), auth=auth)

    # Convert status to string as its an INT
    print('STATUS CODE: ' + str(response.status_code))

    print('RESPONSE:')
    # Print results.text which would have the result. First, assign it to results.
    results = json.loads(response.text)
    # then pretty it a little. Use JSON format and indent by 4 spaces.
    print(json.dumps(results, indent=4))

    # As this script can take arguments, here's some examples:
    # python script "show version"
    # python script "show version" "cli_show_ascii"
    # python script "vlan 10 ;vlan 20 ;vlan 30 ;exit" "cli_conf"
