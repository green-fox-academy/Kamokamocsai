# Write a program that reads a number form the standard input,
# Than prints "Odd" if the number is odd, or "Even" it it is even.
x = int(input("Write a number: "))

if x % 2 == 0:
    print("Even")
elif x % 2 != 0:
    print("Odd")