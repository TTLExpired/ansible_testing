# A sample family dictionary
import yaml

family = {}
person = {}

family_name = input("Enter Family Name: ")

while True:
    try:
        if int(family_name):
            family_name = input("Strings only please: ")
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

    fname = input("Name? ")
    age = input("Age? ")
    city = input("City of Birth? ")

    person[member] = {'name': fname, 'age': age, 'city': city}

family[family_name] = person

print(yaml.dump(family, default_flow_style=False))
