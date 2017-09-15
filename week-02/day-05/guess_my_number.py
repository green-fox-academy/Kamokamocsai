from random import randint

random_number = randint(1, 100)

user_guess = int(0)

def guessed(user_guess):
    user_life = 20
    while not user_guess == random_number:
        user_guess = int(input("Pick a number between 1 and 100: "))
        if user_guess == random_number:
            print("Congratulations! You won!")
        elif user_guess > random_number:
            user_life = user_life - 1                    
            print("Too high! You have " + str(user_life) + " lives left.")
        else:
            user_life -= 1
            print("Too low! You have " + str(user_life) + " lives left.")
        
guessed(user_guess)