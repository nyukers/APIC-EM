# Request configuration.
#
# APIC-EM Workshop, 2020

import requests,json,datetime,re

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

def get_config2(token, url):

     # Define API Call. To get specific device's configuration.
     # Add device's ID in the API call.
     api_call = "/network-device/config"

     # Header information.
     headers = {"X-AUTH-TOKEN": token}

     # Combine URL, API call variables.
     url += api_call

     response = requests.get(url, headers=headers, verify=False).json()
	 
     for data in response['response']:
         # Find the hostname in the response body and save it to a hostname variable.
         hostname = re.findall('hostname\s(.+?)\s', data['runningConfig'])[0]

         # Create a date_time variable which will hold current time.
         date_time = datetime.datetime.now()

         # Create a variable which will hold the hostname combined with the date and time.
         # The format will be hostname_year_month_day_hour.minute.second
         filename = hostname + '_' + str(date_time.year) + '_' + str(date_time.month) + '_' + str(date_time.day)
		 #+ '_' + str(date_time.hour) + '.' + str(date_time.minute) + '.' + str(date_time.second)

         # Create a file in present working directory.
         file = open(filename, 'w')       
         file.write(data['runningConfig'])
         # Close the file when writing is complete.
         file.close()
		 
# Assign obtained authentication token to a variable. Provide APIC-EM's URL address.
auth_token = get_token(apic_em_ip)

# Call get_config() function to obtain and write each network device's configuration to a separate file.
#Provide authentication token, APIC-EM's URL address

#get_config(auth_token, apic_em_ip)

get_config2(auth_token, apic_em_ip)
