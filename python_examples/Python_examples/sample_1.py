# A quick script to input n number in a list and display them.
# Not sure if this is going to work as it shouuld.
# TODO: Check this also works.

List = []
ListLength = input("How many entries in your list? ")

while True:
    try:
        Check_Value = int(ListLength)
        if Check_Value:
            print("You entered {}. Will proceed.".format(Check_Value))
            break
    except ValueError:
        ListLength = input("How many entries in your list? ")

print("We'll input {}".format(ListLength))
for i in range(int(ListLength)):

    while True:
        ListValue = input("Enter Number: ")
        try:
            if int(ListValue):
                List.append(ListValue)
                break
        except ValueError:
            ListValue = input("Numbers only!: ")

print("The list is {}".format(List))
