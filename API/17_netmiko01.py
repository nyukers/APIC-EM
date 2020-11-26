#!/usr/bin/env python
# netmiko

from netmiko import ConnectHandler
from jinja2 import Environment, FileSystemLoader

device = ConnectHandler(host='veos', username='ntc', password='ntc123', device_type='arista_eos')
interface_dict = {
    "name": "Ethernet6",
    "description": "Server Port",
    "vlan": 10,
    "uplink": False
    }

ENV = Environment(loader=FileSystemLoader('.'))
template = ENV.get_template("config.j2")
commands = template.render(interface=interface_dict)

with open('veos.conf', 'w') as config_file:
    config_file.writelines(commands)

output = device.send_config_from_file('veos.conf')
verification = device.send_command('show run interface Eth6')
print(verification)

device.disconnect()