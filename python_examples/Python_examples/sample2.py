# A simple script to enter dictionary data of family members.

Family_Members = {}

Family_Members['Name'] = input("Enter Name: ")
try:
    if int(Family_Members['Name']):
        Family_Members['Name'] = input("Names only at this stage: ")
except ValueError:
    pass
