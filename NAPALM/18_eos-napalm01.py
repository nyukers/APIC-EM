device.load_merge_candidate(filename='snmp.conf')

diffs = device.compare_config()

print(diffs)
