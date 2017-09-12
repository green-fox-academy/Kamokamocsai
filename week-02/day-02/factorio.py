
# - Create a function called `factorio`
#   that returns it's input's factorial
def factorio(num):
    for i in range(1, num):
        num = num * i
    return num


print(factorio(5))  