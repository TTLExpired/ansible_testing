# Adding ospf statements from ospf yaml file.
import json
import requests
from requests.auth import HTTPBasicAuth
import yaml


if __name__ == "__main__":

    auth = HTTPBasicAuth('mossesb', 'password')
    headers = {
            'Accept': 'application/vnd.yang.data+json',
            'Content-Type': 'application/vnd.yang.data_json'
            }

    url = 'http://172.16.7.251/restconf/api/config/native/router'

    ospf_config = yaml.load(open('ospf_add_nets.yml').read())

    ospf_object_to_send = {
            "ned:router": ospf_config
            }

    response = requests.patch(url, data=json.dumps(ospf_object_to_send),
                                headers = headers, auth=auth)

    print(response.status_code)
