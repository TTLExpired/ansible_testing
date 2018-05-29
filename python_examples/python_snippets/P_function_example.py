'''
A generic script that would check for:
    Yourname
    Age
    Date of Birth
The Important part is the functions. Just mocking around.
'''
from string import ascii_letters
from datetime import datetime


def check_number(integer_value):
    '''
    Check if the input is a digit.
    '''
    while True:
        try:
            if int(integer_value):
                break
        except ValueError:
            integer_value = input("Numbers only please: ")

    return integer_value


def check_string(string_value):
    '''
    Check if the input is a string.
    '''
    allowd_chars = ascii_letters 

    while True:
        if all(c in allowd_chars for c in string_value):
            break
        else:
            string_value = input("Strings only buddy: ")

    return string_value


def check_date(date_value):
    '''
    Check if date is the correct format.
    '''
    while True:
        try:
            correct_date = datetime.strptime(date_value, '%d/%m/%Y')
            break
        except ValueError:
            date_value = input("Date format is DD/MM/YYYY ")

    return correct_date


def print_data(integer_value, string_value, age_value):
    '''
    We now print all three values after they've been checked.
    '''
    print("Hello Mr {}. You're {} old, and born on {}".
          format(integer_value, string_value, age_value))


def main():
    '''
    Our main function. Get input.
    '''
    first_name = input("What's your name kind Sir? ")
    check_string(first_name)

    the_age = input("And what is your age? ")
    check_number(the_age)

    date_of_birth = input("And when were you born? ")
    check_date(date_of_birth)

    # We now send everything to print
    print_data(first_name, the_age, date_of_birth)


if __name__ == "__main__":
    main()
