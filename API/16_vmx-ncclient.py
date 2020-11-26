#!/usr/bin/env python
# ncclient vMX

from ncclient import manager

vmx = manager.connect(host='junos-vmx', port=830, username='ntc',
                      password='ntc123', hostkey_verify=False,
                      device_params={},
                      allow_agent=False, look_for_keys=False)

get_filter = """
<configuration>
  <snmp>
  </snmp>
</configuration>
"""

nc_get_reply = vmx.get(('subtree', get_filter))
print(nc_get_reply.xml)