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


print(" +++ Welcome to IOS writer +++")
print(" IF you make a mistake at any time, press ctrl+c")
print("let's begin")
print('*'*60)

# Hostname and SNMP Chassis ID
hostname = input("Hostname? ")

snmpid = input("Use hostname for snmp chassis-ID [Y/N]? ")
if snmpid.lower() in ['yes', 'y']:
    snmpchassis = hostname
else:
    snmpchassis = input(" Snmp Chassis-id? ")
print("chassis id is {}".format(snmpchassis))

timezone = input("Timezone? ")
fqdn = input(" Domain Name? ")
if hostname.lower() in fqdn:
    fqdn = input("Please enter domain name without hostname: ")
else:
    pass
if timezone == 'ADST +10':
    recurr = 'ADST recurring 1 Sun Oct 2:00 1 Sun Apr 3:00'

stream = open('config.yaml', 'w')
yaml.dump({'system': {'name': hostname, 'location': snmpchassis,
                      'tz': timezone, 'fqdn': fqdn, 'recurr': recurr }},
            stream, default_flow_style=False)

"""
print(yaml.dump({'system': {'name': hostname, 'location': snmpchassis}},
                default_flow_style=False))
"""
