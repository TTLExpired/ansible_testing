# A script to try and add data to template.js using python classmethod 
# We first load Jinja environment and filesystemloader modules
from jinja2 import Environment, FileSystemLoader

# We define the template as existing in same directory as this script
ENV = Environment(loader=FileSystemLoader('.'))

# Use ENV template to derive a template 'OBJECT'
template = ENV.get_template("template.j2")


class NetworkInterface(object):
    # First the construct. Simple. Only four values
    def __init__(self, name, description, vlan, uplink=False):
        self.name = name
        self.description = description
        self.vlan = vlan
        self.uplink = uplink

# We now poplute interface_obj with the 3 values from the class
interface_obj = NetworkInterface("GigabitEthernet0/1", "Server Port", 10)

# Assin the values with interface_obj to the template
print(template.render(interface=interface_obj))
