#!/usr/bin/env python

import json
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
   auth = HTTPBasicAuth('ntc', 'ntc123')
   headers = {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
   }

url = "https://asav/api/interfaces/physical"
response = requests.get(url, auth=auth, headers=headers, verify=False)
