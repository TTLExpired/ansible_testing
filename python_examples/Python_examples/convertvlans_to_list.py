# A simple script that turns vlans.cfg file into dictionary.


# Read the file, copy content into a list and last,
# update the list to get rid of \n.
vlans_file = open('vlans.cfg', 'r')
vlans_text = vlans_file.read()
vlans_list = vlans_text.splitlines()

# You can combine the above
# vlans_list = open('vlans.cfg', 'r').splitlines()

# Now we convert it into dictionary
vlans = []

for item in vlans_list:
    if 'vlan' in item:
        # Create a temp dictrionary
        temp = {}
        # remove space, then vlan, leaving the 'number' without space.
        # within 'temp {} dictionary, add the first key id:vlan id'
        # id is then = vlan id
        id = item.strip().strip('vlan').strip()
        temp['id'] = id
    elif 'name' in item:
        # Do exactly the same thing, this time strip all the way
        # to name and from there, add a new key 'name' and value
        # the vlaue 'name' string
        name = item.strip().strip('vlan').strip()
        temp['name'] = name
        # We're systamtically appending vlans LIST item. Howerver,
        # temp here is a dictionary with each having two keys
        # and two values, ID and Name.
        vlans.append(temp)

vlans_file.close()

# Lets print and see what happens
print ('Here is a list of VLANS')
print(*vlans, sep='\n')

# We now write the new list to a file
# Python would create the file if needed
write_file = open('formated_vlans.cfg', 'w')

# We get the list and loop throug it.
for vlan in vlans:
    # Get the vlan ID number
    id = vlan.get('id')
    # Get the vlan name
    name = vlan.get('name')
    # Simply write 'vlan' followed by its ID and 'enter'
    write_file.write('vlan ' + id + '\n')
    # In the new line line, write 'name' followed by its name and 'enter'
    write_file.write('  name ' + name + '\n')

# Close the file
write_file.close()
