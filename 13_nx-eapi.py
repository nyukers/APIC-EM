#!/usr/bin/env python
# Arista eAPI Command Explorer 
# HTTP POST

import json
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    auth = HTTPBasicAuth('ntc', 'ntc123')
    url = 'http://eos-spine1/command-api'
    payload = {
        "jsonrpc": "2.0",
        "method": "runCmds",
        "params": {
            "format": "json",
            "timestamps": False,
        "cmds": [
            "show vlan brief"
        ],
        "version": 1
    },
    "id": "EapiExplorer-1"
}    	

response = requests.post(url, data=json.dumps(payload), auth=auth)
print('STATUS CODE: ' + response.status_code)
print('RESPONSE:')
results = json.loads(response.text)
print(json.dumps(results, indent=4))
