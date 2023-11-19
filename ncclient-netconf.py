import xml.dom.minidom
from ncclient import manager
import requests


m = manager.connect(
    host="192.168.10.128",
    port=830,
    username="cisco",
    password="cisco123!",
    hostkey_verify=False
    )
'''
print("#Supported Capabilities (YANG models):")
for capability in m.server_capabilities:
    print(capability)
'''

netconf_filter = """
<filter>
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" />
</filter>
"""

netconf_hostname = """

<config>

 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">

  <hostname>WOWLOOKATTHAT</hostname>

   </native>

   </config>
"""
   

netconf_loopback = """
<config>
<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
 <interface>
 <Loopback>
 <name>2</name>
 <description>Luke's Cool NETCONF loopback</description>
 <ip>
 <address>
 <primary>
 <address>192.168.34.10</address>
 <mask>255.255.255.0</mask>
 </primary>
 </address>
 </ip>
 </Loopback>
 </interface>
</native>
</config>
"""

netconf_reply = m.edit_config(target="running", config=netconf_loopback)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

access_token = 'NGJhMTM4OTktMTZlNi00NGI1LWJkOTItNWM1OGJjN2I5Mjg0ZDM3ZGI0YmQtMWI1_P0A1_1fd0570a-c6cc-44c3-b853-8fc8a6f6f0a4'
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vZTM2MTM4ZTAtODI5ZC0xMWVlLThjZjYtZTM3NzM0MDEyYWJm'
message = 'Hello Everyone the NETCONF program successfully ran!!'
url = 'https://webexapis.com/v1/messages'
headers = {
 'Authorization': 'Bearer {}'.format(access_token),
 'Content-Type': 'application/json'
}
params = {'roomId': room_id, 'markdown': message}
res = requests.post(url, headers=headers, json=params)
print(res.json())





