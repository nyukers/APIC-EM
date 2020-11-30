dir(device)

device.get_facts()

device.get_snmp_information()

device.get_lldp_neighbors()

for interface, neighbors in device.get_lldp_neighbors().items():
    print("INTERFACE: " + interface)
    print("NEIGHBORS: ")
    for neighbor in neighbors:
        print(" - {}".format(neighbor['hostname']))
        
