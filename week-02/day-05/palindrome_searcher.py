user_input = input("Add words and search palindromes:")


def search_palindrome(user_input):
    output = []
    for i in range(len(user_input)-1, 0, -1):
        for j in range(i):
            x = user_input[j:i]
            if x == x[::-1]:
            # print(user_input[j])
                output.append(x)  
                    
        print(output)
    
search_palindrome(user_input)

# def create_palindrome(user_input, user_input_reversed):
#     palindrome = user_input + user_input_reversed
#     print(palindrome)
# create_palindrome(user_input, user_input_reversed)