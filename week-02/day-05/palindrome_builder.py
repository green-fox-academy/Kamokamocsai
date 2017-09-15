user_input = input("Pls add a word for create a palindrome: ")
user_input_reversed = user_input[::-1]

def create_palindrome(user_input, user_input_reversed):
    palindrome = user_input + user_input_reversed
    print(palindrome)

create_palindrome(user_input, user_input_reversed)