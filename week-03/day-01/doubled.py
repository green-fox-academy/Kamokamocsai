# Create a method that decrypts the duplicated-chars.txt



def decrypt(file_name):
    opened = open(file_name, 'r')
    new_text = open("new_text.txt", "w")
    for i in opened:
        temp = ""
        temp += i[::2]
        new_text.write(temp)
    opened.close()
    new_text.close()



decrypt("dublicated-chars.txt")