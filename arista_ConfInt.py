# A script to configure an interface based on LLDP
import json
import sys
import requests
from requests.auth import HTTPBasicAuth


def issue_request(device, commands):
    #Make API request to EOS device with JSON response

    auth = HTTPBasicAuth('mossesb', 'password')

    url = 'http://{}/command-api'.format(device)
    payload = {
            "jsonrpc": "2.0",
            "method": "runCmds",
            "params": {
                "format": "json",
                "timestamps": "False",
                "cmds": commands,
                "version": 1
                },
                "id": "EapiExplorer-1"
            }
    response = request.post(url, data=json.dumps(payload), auth=auth)

    return json.loads(response.text)


def get_lldp_neighbors(device):
    #Get List of neighbours
    commands = ['show lldp neighbors']
    response = issue_request(device, commands)
    neighbors = response['result'][0]['lldpNeighbors']

    return neighbours


def configure_interfaces(device, neighbors):
    #Cofigure Interfaces based on return LLDP data
    command_list = ['enable', 'configure']
    for neighbor in neighbors:
        local_interface = neighbor['port']
        if local_interface.startwith('Eth'):
            #Exclude Management
            description = 'Link to {} router {}'.format(
                    neighbor['neighborPort'],
                    neighbor['neighborDevice'])
            description = 'description ' + description

            interface = 'interface {}'.format(local_interface)
            cmds = [interface, description]
            command_list.extend(cmds)
    response = issue_request(device, command_list)


if __name__ == "__main__":
    devices = ['10.0.7.254', '10.0.7.253']
    for device in devices:
        neighbors = get_lldp_neighbors(device)
        configure_interfaces(device, neighbors)
        print('Auto-Configured interfaces for {}'.format(device))
