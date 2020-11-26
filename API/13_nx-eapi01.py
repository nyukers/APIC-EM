#!/usr/bin/env python
# Arista eAPI Command Explorer 
# HTTP POST

import json
import sys
import requests
from requests.auth import HTTPBasicAuth

def issue_request(device, commands):
    """Make API request to EOS device returning JSON response
       (Ñîçäàíèå çàïðîñà API ê óñòðîéñòâó EOS, âîçâðàùàþùåìó îòâåò â ôîðìàòå JSON)
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
(Ïîëó÷åíèå ñïèñêà ñîñåäíèõ óñòðîéñòâ
Sample response for a single neighbor:
Àâòîìàòèçàöèÿ ñ èñïîëüçîâàíèåì ñåòåâûõ API ? 281
(Ïðèìåð îòâåòà îò îäíîãî èç ñîñåäíèõ óñòðîéñòâ:)
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
# ñîñåäíèå óñòðîéñòâà (èìåíà) âîçâðàùàþòñÿ â âèäå ñïèñêà ñëîâàðåé
return neighbors

def configure_interfaces(device, neighbors):
"""Configure interfaces in a single API call per device
(Êîíôèãóðèðîâàíèå èíòåðôåéñîâ â îäíîì âûçîâå API äëÿ êàæäîãî óñòðîéñòâà)
"""
command_list = ['enable', 'configure']
for neighbor in neighbors:
    local_interface = neighbor['port']
    if local_interface.startswith('Eth'):
        # Ïðîõîä ñ ó÷åòîì ñóùåñòâóþùèõ ñîñåäíèõ óñòðîéñòâ
        description = 'Connects to interface {} on neighbor {}'.format(
            neighbor['neighborPort'],
            neighbor['neighborDevice'])
        description = 'description ' + description
        interface = 'interface {}'.format(local_interface)
        cmds = [interface, description]
        command_list.extend(cmds)
response = issue_request(device, command_list)

if __name__ == "__main__":
    # Èìåíà óñòðîéñòâ ÿâëÿþòñÿ ïîëíûìè äîìåííûìè èìåíàìè FQDN
    devices = ['eos-spine1', 'eos-spine2']
    for device in devices:
        neighbors = get_lldp_neighbors(device)
        configure_interfaces(device, neighbors)
        print('Auto-Configured Interfaces for {}'.format(device))
