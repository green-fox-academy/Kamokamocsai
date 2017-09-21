# We have a number of bunnies and each bunny has two big floppy ears.
# We want to compute the total number of ears across all the bunnies recursively (without loops or multiplication).

def total_bunny_ears(bunnies):
    ears = 2
    if bunnies == 0:
        return bunnies
    else:
        return ears + total_bunny_ears(bunnies - 1)

print(total_bunny_ears(20))