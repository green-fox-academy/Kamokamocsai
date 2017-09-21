# Given a non-negative int n, return the sum of its digits recursively (no loops). 
# Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while 
# divide (/) by 10 removes the rightmost digit (126 // 10 is 12).

def number_adder(number):
    if number < 10:
        return number
    else:
        return number % 10 + number_adder(number // 10)

sum_total = number_adder(434)
print(sum_total)