#!/usr/bin/env python
# ncclient IOS-XE

from ncclient import manager
from lxml import etree

get_filter = """
    <native xmlns="http://cisco.com/ns/yang/ned/ios">
    <interface>
    <GigabitEthernet>
    <name>1</name>
    </GigabitEthernet>
    </interface>
    </native>
    """

nc_get_reply = device.get(('subtree', get_filter))

print(nc_get_reply)

type(nc_get_reply)
type(nc_get_reply.data)
type(nc_get_reply.data_ele)

print(nc_get_reply.data_ele)

as_string = etree.tostring(nc_get_reply.data)
print(as_string)

as_string = etree.tostring(nc_get_reply.data, pretty_print=True)
print(as_string)

type(nc_get_reply.xml)
print(nc_get_reply.xml)

as_object = etree.fromstring(nc_get_reply.xml)
print(as_object)

primary = nc_get_reply.data.find('.//{http://cisco.com/ns/yang/ned/ios}primary')
primary = nc_get_reply.data.find('.//primary')

ipaddr = primary.find('.//{http://cisco.com/ns/yang/ned/ios}address')
ipaddr.text

mask = primary.find('.//{http://cisco.com/ns/yang/ned/ios}mask')
mask.text
