# Write a program that asks for two numbers
# Thw first number represents the number of girls that comes to a party, the
# second the boys

girls = int(input("How many girls: "))
boys = int(input("How many boys: "))

# It should print: The party is exellent!
# If the the number of girls and boys are equal and there are more people coming than 20

if girls == boys and girls + boys > 20:
    print("The party is excellent!")

#
# It should print: Quite cool party!
# It there are more than 20 people coming but the girl - boy ratio is not 1-1
#

if girls != boys and girls + boys > 20:
    print("Quite cool party!")

# It should print: Average party...
# If there are less people coming than 20
#
# if girls == 0:
if girls == 0:
    print("Sausage party")

elif girls + boys < 20:
    print("Average party...")

# It should print: Sausage party
# If no girls are coming, regardless the count of the people
