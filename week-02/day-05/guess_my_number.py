from random import randint

random_number = randint(1, 100)

user_life = 5
user_guess = int(0)

def guessed(user_guess):
    user_guess = int(input("Pick a number between 1 and 100: "))
    if user_guess == random_number:
        print("Congratulations! You won!")
    elif user_guess > random_number:
        print("Too high! You have x lives left.")
    elif user_guess < random_number:
        print("Too low! You have x lives left.")
    return user_guess

guessed(user_guess)