#!/usr/bin/env python
# RESTCONF API IOS-XE

import json
import requests
from requests.auth import HTTPBasicAuth
import yaml

if __name__ == "__main__":
    auth = HTTPBasicAuth('ntc', 'ntc123')
    headers = {
        'Accept': 'application/vnd.yang.data+json',
        'Content-Type': 'application/vnd.yang.data+json'
    }
    url = 'http://ios-csr1kv/restconf/api/config/native/router'
    ospf_config = yaml.load(open('ospf-config.yml').read())
    ospf_object_to_send = {
        "ned:router": ospf_config
    }
    response = requests.patch(url, data=json.dumps(ospf_object_to_send), headers=headers, auth=auth)
    print(response.status_code)

-OR-

    response = requests.patch(url, data=json.dumps(ospf_object_to_send), headers=headers, auth=auth)
    print(response.status_code)
