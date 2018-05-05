# Testing functions
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

AssignedValue = input("What's the community String? ")
AssignedValue = GetValue(AssignedValue)
print(AssignedValue)
    
