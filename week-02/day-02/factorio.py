
# - Create a function called `factorio`
#   that returns it's input's factorial

number = int(input("Please add a number: "))

def factorio(num):
    for i in range(1, num):
        num = num * i
    return num


print(factorio(number))  