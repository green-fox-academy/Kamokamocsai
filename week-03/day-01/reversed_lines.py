# Create a method that decrypts reversed-lines.txt
def decrypt(file_name):
    opened = open(file_name, "r")
    solution = open('solution.txt', 'w')
    for i in opened:
        temp = ""
        temp = i[::-1]
        print(temp)
        solution.write(temp)
    opened.close()
    solution.close


decrypt("reversed-lines.txt")