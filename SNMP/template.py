from jinja2 import Environment, FileSystemLoader

ENV = Environment(loader=FileSystemLoader('./templates'))
template = ENV.get_template("template.j2")

interface_dict = {
    "name": "GigabitEthernet0/1",
    "description": "Server Port",
    "vlan": 10,
    "uplink": False
}

print(template.render(interface=interface_dict))

# interface GigabitEthernet0/1
# description Server Port
# switchport access vlan 10
# switchport mode access

