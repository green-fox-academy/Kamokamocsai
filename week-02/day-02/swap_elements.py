# - Create a variable named `abc`
#   with the following content: `["first", "second", "third"]`
# - Swap the first and the third element of `abc`

abc = ["first", "second", "third"]

def swapper(elements):
    elements[0], elements[2] = elements[2], elements[0]

print(swapper(abc))