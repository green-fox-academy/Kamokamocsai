user_input_1 = input("Pls write a word: ")
user_input_2 = input("Pls write another word: ")
user_input_1_reversed = user_input_1[::-1]

def anagram(user_input_1, user_input_2):
    if user_input_1_reversed == user_input_2:
        print(True)
    else:
        print(False)

anagram(user_input_1, user_input_2)