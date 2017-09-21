# We have bunnies standing in a line, numbered 1, 2, ... The odd bunnies
# (1, 3, ..) have the normal 2 ears. The even bunnies (2, 4, ..) we'll say
# have 3 ears, because they each have a raised foot. Recursively return the
# number of "ears" in the bunny line 1, 2, ... n (without loops or multiplication).

def bunny_ears_counter(number):
    odd_bunny_ears = 2
    even_bunny_ears = 3
    if number == 1:
        return number
    elif number % 2 == 0:
        return even_bunny_ears + bunny_ears_counter(number - 1)
    else:
        return even_bunny_ears + bunny_ears_counter(number - 1)


print(bunny_ears_counter(5))