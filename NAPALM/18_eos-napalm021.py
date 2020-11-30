device.load_merge_candidate(filename='ospf.conf')

diffs = device.compare_config()

print(diffs)
