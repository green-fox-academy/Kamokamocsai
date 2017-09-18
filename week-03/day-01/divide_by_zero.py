# create a function that takes a number,
# divides ten with it,
# and prints the result.
# it should print "fail" if the parameter is 0

number = int(input("Add a number: "))

def divide(number):
    try:
        divided_number = 10 /number
        print(divided_number)
    except ZeroDivisionError:
        print("fail")

divide(number)