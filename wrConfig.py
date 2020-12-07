# Request configuration.
#
# APIC-EM Workshop, 2020

import requests
import json

# Disable warnings.
requests.packages.urllib3.disable_warnings()

# Variables
apic_em_ip = "https://sandboxapicem.cisco.com/api/v1"

def get_token(url):

    # Define API Call to get authentication token.
    api_call ="/ticket"

    # Payload contains authentication information.
    payload = { "username": "devnetuser", "password": "Cisco123!" }

    # Header information.
    headers = {"content-type" : "application/json"}

    # Add the API call to the URL argument.
    url +=api_call

    response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False).json()

    # Return authentication token from respond body.
    return response["response"]["serviceTicket"]



def get_config(token, url):

    # Define the API Call. Get configuration for all network devices.    
    api_call = "/network-device/config"

    # Header
    headers = {"X-AUTH-TOKEN": token}

    # Combine URL, API call variables.
    url += api_call

    response = requests.get(url, headers=headers, verify=False).json()
    count=1
    for data in response['response']:
        filename="access_host_" + str(count) +".txt"

        # Create a file in present working directory.
        file = open(filename, 'w')       

        # write json data from runningConfig key.
        file.write(data['runningConfig'])

        # Close the file when writing is complete.
        file.close()
        count+=1

# Assign obtained authentication token to a variable. Provide APIC-EM's URL address.
auth_token = get_token(apic_em_ip)

# Call get_config() function to obtain and write each network device's configuration to a separate file.
#Provide authentication token, APIC-EM's URL address
get_config(auth_token, apic_em_ip)