# Write a function that copies a file to an other
# It should take the filenames as parameters
# It should return a boolean that shows if the copy was successful

file_from = input("Filename want to copy?: ")
file_to = input("Copy to...: ")

def copy_file(file_from, file_to):
    try:
        text1 = open(file_from, 'r')
        all_text = text1.read()
        copy_where = open(file_to, 'w')
        copy_where.write(all_text)
        text1.close()
        copy_where.close()
        print(True)
    except FileNotFoundError:
        print(False)

copy_file(file_from, file_to)
