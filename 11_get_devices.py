#
#This script prints out all network devices that are connected to APIC-EM network devices in a tabular list format.
#

import requests
import json
from tabulate import *
from apic_em_functions import *

api_url = "https://sandboxapicem.cisco.com/api/v1/network-device"

# Setup API request headers.
ticket = get_ticket()
headers = {
    "content-type": "application/json",
    "X-Auth-Token": ticket
}

resp = requests.get(api_url, headers=headers, verify=False)
# This is the http request status
print("Status of device request: ", resp.status_code)
# Check if the request status was 200/OK
if resp.status_code != 200:
    raise Exception("Status code does not equal 200. Response text: " + resp.text)

# Get the json-encoded content from response
response_json = resp.json()


# Now create a list of host summary info
device_list = []
i = 0
for item in response_json["response"]:
    i += 1
    device = [
                i, 
                item["type"], 
                item["managementIpAddress"] 
             ]
    device_list.append( device )

table_header = [
                "#", 
                "Type", 
                "IPv4"
               ]
print(tabulate(device_list, table_header))
