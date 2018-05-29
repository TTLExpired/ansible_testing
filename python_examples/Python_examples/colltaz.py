'''
A Python script to try Collatz equation.
called the simplist impossible math problem.
not sure how it works yet.
but i'll give it a try.
'''


def testme(number):
    print("Let's devide it by 2: ")
    EvenorOdd = number % 2

    if EvenorOdd == 0:
        print("Perfect Division.  Let's devide it again by 2!")
        number = number / 2
    else:
        print("Mmm. Let's take the number {} and * 3 Plus 1. ".format(number))
        number = 3 * number + 1

    return number


def main():
    xnumber = int(input('Give me a number. Any Number :'))

    while xnumber > 1:
        xnumber = testme(xnumber)
        print("And now it's:  {}".format(xnumber))

    print("And you're left with::: {}".format(xnumber))
    print("No matter what number you enter -:)")


if __name__ == "__main__":
    main()
