
vmx = manager.connect(host='junos-vmx', port=830, username='ntc',
                      password='ntc123', hostkey_verify=False,
                      device_params={'name': 'junos'},
                      allow_agent=False, look_for_keys=False)

nxos = manager.connect(host='nxos1', port=22, username='ntc',
                       password='ntc123', hostkey_verify=False,
                       device_params='name': 'nexus'},
                       allow_agent=False, look_for_keys=False)

hpe = manager.connect(host='hpe5930', port=830, username='ntc',
                      password='ntc123', hostkey_verify=False,
                      device_params={'name': 'hpcomware'},
                      allow_agent=False, look_for_keys=False)
