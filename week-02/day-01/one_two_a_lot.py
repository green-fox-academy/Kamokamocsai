# Write a program that reads a number form the standard input,
# If the number is zero or smaller it should print: Not enough
# If the number is one it should print: One
# If the number is two it should print: Two
# If the number is more than two it should print: A lot
x = int(input("1 or 2: "))

if x <= 0:
    print("Not enough")
elif x == 1:
    print("One")
elif x == 2:
    print("Two")
elif x > 2:
    print("A lot")