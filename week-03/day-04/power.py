# Given base and n that are both 1 or more, compute recursively (no loops)
# the value of base to the n power, so powerN(3, 2) is 9 (3 squared).

def power_number(base, number):
    if number == 1:
        return base * number
    else: 
        return base * power_number(base, number - 1)


print(power_number(6, 6))