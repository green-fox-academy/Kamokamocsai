user_input = input()

def armstronger(user_input):
    solution = 0
    length = len(user_input)
    for i in range(length):
        solution += int(user_input[i]) ** length
    if solution == int(user_input):
        print("The " + str(solution) + " is an Armstrong number.")
    else:
        print(str(user_input) + " is not an Armstrong number.")
armstronger(user_input)
