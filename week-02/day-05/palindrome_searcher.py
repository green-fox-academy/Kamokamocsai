user_input = input("Add words to search palindromes:")


def search_palindrome(user_input):
    for i in range (0, (len(user_input) + 1) / 2):
        if user_input[i] != user_input[i]:
            return False
    return True      
    
search_palindrome(user_input)

output = []

print(output)