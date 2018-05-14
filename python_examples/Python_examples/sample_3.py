# A sample family dictionary

family = {}
members = {}

family['family_name'] = input("Enter Family Name: ")

while True:
    try:
        if int(family['family_name']):
            family['family_name'] = input("Strings only please: ")
    except ValueError:
        break

FamilyMembers = input("How many members for this dictionary? ")

while True:
    try:
        if int(FamilyMembers) >= 1:
            print("We'll continue for {} members".format(FamilyMembers))
            break
    except ValueError:
        FamilyMembers = input("Numbers only Please: ")

# We now start to loop for each members:
for member in range(int(FamilyMembers)):
    family[member] = {
                'fname': input("Enter Name: "),
                'age': input("Enter Agre: "),
                'city': input("Enter City of Birth: ")
                }

print("Here's what we have so far {} ".format(family))
