# Write a program that asks for 5 integers in a row,
# then it should print the sum and the average of these numbers like:
#
# Sum: 22, Average: 4.4
a = int(input("Pls write the first number: "))
b = int(input("Pls write the second number: "))
c = int(input("Pls write the third number: "))
d = int(input("Pls write the 4th number: "))
e = int(input("Pls write the 5th number: "))

sum = float((a + b + c + d + e) / 5)
print(float(sum))