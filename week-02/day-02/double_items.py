# - Create an array variable named `ag`
#   with the following content: `[3, 4, 5, 6, 7]`
# - Double all the values in the array

ag = [3, 4, 5, 6, 7]

def double_ag(list_of_numbers):
    for i in range(len(list_of_numbers)):
        list_of_numbers[i] *= 2
    return list_of_numbers

print(double_ag(ag))