# Open a file called "my-file.txt"
# Write your name in it as a single line
# If the program is unable to write the file,
# then it should print an error message like: "Unable to write file: my-file.txt"

user_name = input("What\'s your name? ")

try:
    text_file = open('my-file.txt', 'r')
    text_file.write(user_name)
    text_file.close()
except:
    print("Unable to write file: my-file.txt")