# 
# Prints out all hosts that are connected to APIC-EM network devices in a tabular list format.
# Some functions have dependencies.
#
# APIC-EM Workshop, 2020

__author__ = 'Nyukers'

import requests
import json
from tabulate import *
from apic_em_functions import *

api_url = "https://sandboxapicem.cisco.com/api/v1/host"

# All APIC-EM REST API request and response content type is JSON.
ticket = get_ticket()
headers = {
    "content-type": "application/json",
    "X-Auth-Token": ticket
}

resp = requests.get(api_url, headers=headers, verify=False)

# This is the http request status
print("Status of host request: ", resp.status_code)

# Check if the request status was 200/OK
if resp.status_code != 200:
    raise Exception("Status code does not equal 200. Response text: " + resp.text)

# Get the json-encoded content from response
response_json = resp.json()

# Create a list of host info to be held in host_list
host_list = []
i = 0
for item in response_json["response"]:
    i += 1
    host = [
            i, 
            item["hostType"], 
            item["hostIp"] 
           ]
    host_list.append( host )

table_header = [
                "#",
                "Type",
                "IPv4"
               ]
#print(tabulate(host_list, table_header))
#print(tabulate(host_list, table_header, tablefmt="grid"))
print(tabulate(host_list, table_header, tablefmt="rst"))


