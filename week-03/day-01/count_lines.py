# Write a function that takes a filename as string,
# then returns the number of lines the file contains.
# It should return zero if it can't open the file, and
# should not raise any error.
    
filename = input("Open text file: ")

def file_object(filename):
    try:
        text = open(filename, "r")
        print(len(text.readlines()))
    except:
        print(0)
        return

file_object(filename)