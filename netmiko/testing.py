import netmiko
import json

# Lets read the devices
with open('routers.json', 'r') as f:
    devices = json.load(f)

#! Just a quick test for netmiko
for device in devices:
    connection = netmiko.ConnectHandler(**device)
    sh_ver = connection.send_command('show version')
    hostname = connection.base_prompt

    sh_ver_list = sh_ver.splitlines()
    for key in sh_ver_list:
        if 'version' in key.lower():
            words = key.split(',')
            ios_firmware = ' '.join(words[0:2])
            print(hostname + ' ' + ios_firmware)

    connection.disconnect()

''' Here's a small script that would write a json formatted file
    of Interface Status in a dictionary format using netmiko.
'''
int_stats = []
new_list = []
int_dict_stats = {}
for device in devices:
    nc = netmiko.ConnectHandler(**device)
    int_dict_stats[nc.base_prompt] = nc.send_command('sh ip int br | i up').split('\n')
    nc.disconnect()
# Lets see what we can do with this Dictionary.
for key, value in int_dict_stats.items():
    for data in value:
        new_list.append(data.split()[0:2])
    int_dict_stats[key] = new_list
# Lets save the data in Json Format
with open('int_status.json', 'w') as output:
    output.write(json.dumps(int_dict_stats, indent=2))
