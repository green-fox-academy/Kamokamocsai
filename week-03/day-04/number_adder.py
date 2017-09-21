# Write a recursive function that takes one parameter: n and adds numbers from 1 to n.


def number_adder(number):
    sum = number
    if number <= 1:
        return sum
    else:
        return sum + number_adder(number-1)


print(number_adder(5))