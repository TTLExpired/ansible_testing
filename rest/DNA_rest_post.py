import requests
import json

# A quick script to pull status of DNA Always on Farm.
# For now, let's try with simply network-device
# But this is a simple one. This is the base for more.

cisco_url = 'https://sandboxdnac.cisco.com/'
rest_url = 'api/v1/'
devices_url = 'network-device'

url