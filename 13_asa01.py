#!/usr/bin/env python
# HTTP PATCH

import json
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
   auth = HTTPBasicAuth('ntc', 'ntc123')
   headers = {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
   }

   requests.packages.urllib3.disable_warnings()

   payload = {
      "kind": "object#GigabitInterface",
      "interfaceDesc": "Configured by Python"
   }

url = "https://asav/api/interfaces/physical/GigabitEthernet0_API_SLASH_0"
response = requests.patch(url, data=json.dumps(payload), auth=auth, headers=headers, verify=False)
