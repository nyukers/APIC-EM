#!/usr/bin/env python
# Arista eAPI Command Explorer 
# HTTP POST

import json
import sys
import requests
from requests.auth import HTTPBasicAuth

def issue_request(device, commands):
    """Make API request to EOS device returning JSON response
       (—оздание запроса API к устройству EOS, возвращающему ответ в формате JSON)
     """

     auth = HTTPBasicAuth('ntc', 'ntc123')
     url = 'http://{}/command-api'.format(device)
     payload = {
         "jsonrpc": "2.0",
         "method": "runCmds",
         "params": {
             "format": "json",
             "timestamps": False,
             "cmds": commands,
             "version": 1
         },
         "id": "EapiExplorer-1"
     }
     response = requests.post(url, data=json.dumps(payload), auth=auth)
     return json.loads(response.text)

def get_lldp_neighbors(device):
"""Get list of neighbors
(ѕолучение списка соседних устройств
Sample response for a single neighbor:
јвтоматизаци€ с†использованием сетевых API ? 281
(ѕример ответа от одного из соседних устройств:)
    {
      "ttl": 120,
      "neighborDevice": "eos-spine2.ntc.com",
      "neighborPort": "Ethernet2",
      "port": "Ethernet2"
    }
"""
commands = ['show lldp neighbors']
response = issue_request(device, commands)
neighbors = response['result'][0]['lldpNeighbors']
# соседние устройства (имена) возвращаютс€ в виде списка словарей
return neighbors

def configure_interfaces(device, neighbors):
"""Configure interfaces in a single API call per device
( онфигурирование интерфейсов в одном вызове API дл€ каждого устройства)
"""
command_list = ['enable', 'configure']
for neighbor in neighbors:
    local_interface = neighbor['port']
    if local_interface.startswith('Eth'):
        # ѕроход с учетом существующих соседних устройств
        description = 'Connects to interface {} on neighbor {}'.format(
            neighbor['neighborPort'],
            neighbor['neighborDevice'])
        description = 'description ' + description
        interface = 'interface {}'.format(local_interface)
        cmds = [interface, description]
        command_list.extend(cmds)
response = issue_request(device, command_list)

if __name__ == "__main__":
    # »мена устройств €вл€ютс€ полными доменными именами FQDN
    devices = ['eos-spine1', 'eos-spine2']
    for device in devices:
        neighbors = get_lldp_neighbors(device)
        configure_interfaces(device, neighbors)
        print('Auto-Configured Interfaces for {}'.format(device))
