from ncclient import manager
import xml.dom.minidom

# A sample script to understand and play with REST/NETCONF using
# Cisco Always on lab for IOSXE

# Connection Detail
host = 'ios-xe-mgmt.cisco.com'
port = 10000
user = 'root'
password = 'D_Vay!_10&'

# Lets esbalish connection with ncclient. Reminds me of netmiko
connection = manager.connect(host=host,
             username=user,
             password=password,
             port=port,
             hostkey_verify=False)

# Let's retrieve the full config
config = connection.get_config('running')

# Print it, formatted in XML
print(xml.dom.minidom.parseString(config.xml).toprettyxml())

# Close the connection
connection.close_session()