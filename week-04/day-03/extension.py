
# Adds a and b, returns as result
def add(a, b):
    return a + b

# Returns the highest value from the three given params
def max_of_three(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

# Returns the median value of a list given as param
def median(pool):
    return pool[int((len(pool) - 1) / 2)]

# Returns true if the param is a vovel
def is_vowel(char):
    return char.lower() in 'aeiouéáőúűöüóí'

# Create a method that translates hungarian into the teve language
def translate(hungarian):
    # teve = hungarian
    teve = ""
    for char in hungarian:
        if is_vowel(char):
            teve += char+'v'+char
        else:
            teve += char
    return teve
        