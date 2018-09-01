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
