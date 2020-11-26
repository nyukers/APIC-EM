#!/usr/bin/env python
# netmiko

from netmiko import ConnectHandler

device = ConnectHandler(host='veos', username='ntc', password='ntc123', device_type='arista_eos')

dir(device)

device.find_prompt()
output = device.find_prompt()
print(output)

output1 = device.config_mode()
output2 = device.find_prompt()
print(output2)

output = device.send_command('show run')
print(output[:165])

output = device.send_command_expect('end', expect_string='eos-spine1#')
output = device.send_command_timing('end')

commands = ['interface Ethernet5', 'description configured by netmiko', 'shutdown']
output = device.send_config_set(config_commands=commands)
print(output)
