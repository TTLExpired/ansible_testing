# This is generic function test.


def print_name(string):
    ''' Function to simply print string sent to it'''

    print(string)


def main():
    ''' Grab Name and send to print_name '''

    first_name = input("What's your name kind Sir? ")
    print_name(first_name)


if __name__ == "__main__":
    main()
