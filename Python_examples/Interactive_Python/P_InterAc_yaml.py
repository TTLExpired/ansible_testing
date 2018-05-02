import yaml


# Functions
def GetValue(AssignedValue):
    """Confirm if current value is correct
       If not, get new value and return it.
       If yes, return same Value 
    """

    Confirm = input("Is the value correct [Y/N]? ")
    if Confirm.lower() in ['yes', 'y']:
      return AssignedValue
    else:
      AssignedValue = input("Please enter new value: ")

    return AssignedValue


#
################ Start Script #####################################
#

print(" +++ Welcome to IOS writer +++")
print(" IF you make a mistake at any time, press ctrl+c")
print("let's begin")
print('*'*60)

# We get some values. Static for now. Change to function later.
hostname = input("Hostname? ")

snmpid = input("Use hostname for snmp chassis-ID [Y/N]? ")
if snmpid.lower() in ['yes', 'y']:
    snmpchassis = hostname
else:
    snmpchassis = input(" Snmp Chassis-id? ")
print("chassis id is {}".format(snmpchassis))

# Lets try printing - that would be its own function soon.
print("Dumping data to files")

stream = open('config.yaml', 'w')
yaml.dump({'system': {'name': hostname, 'location': snmpchassis}},
            stream, default_flow_style=False)

"""
print(yaml.dump({'system': {'name': hostname, 'location': snmpchassis}},
                default_flow_style=False))
"""
