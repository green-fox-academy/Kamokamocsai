user_input_1 = input()
user_input_2 = input()
user_input_1_reversed = user_input_1[::-1]

def anagram(user_input_1, user_input_2):
    if user_input_1_reversed == user_input_2:
        print(True)
    else:
        print(False)

anagram(user_input_1, user_input_2)