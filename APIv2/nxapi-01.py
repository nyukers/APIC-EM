#
# Developers and network engineers access the "Open NX-OS Programmability" 
#
# For NXAPI to authenticate the client using client certificate, set 'client_cert_auth' to True.
# For basic authentication using username & pwd, set 'client_cert_auth' to False.
#
# APIC-EM Workshop, 2020

import requests
import json

requests.packages.urllib3.disable_warnings()  # Disable SSL warnings

client_cert_auth=False
switchuser='admin'
switchpassword='Admin_1234!'

client_cert='PATH_TO_CLIENT_CERT_FILE'
client_private_key='PATH_TO_CLIENT_PRIVATE_KEY_FILE'
ca_cert='PATH_TO_CA_CERT_THAT_SIGNED_NXAPI_SERVER_CERT'

url='https://sbx-nxos-mgmt.cisco.com/ins'
myheaders={'content-type':'application/json-rpc'}
payload=[
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "show version",
	  #"cmd": "hostname nx-osv-1",
      "version": 1
    },
	"id": 1
  }
]
    

print("URL request: ", url)

if client_cert_auth is False:
    response = requests.post(url, data=json.dumps(payload), headers=myheaders, auth=(switchuser,switchpassword), verify=False).json()
else:
#    url='https://10.10.20.95/ins'
    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword),cert=(client_cert,client_private_key),verify=ca_cert).json()
	
#print("Content of request: ", response['result']['body']['header_str'])
print("Current version is: ", response['result']['body']['nxos_ver_str'])