# Write a program that stores 3 sides of a cuboid as variables (doubles)
# The program should write the surface area and volume of the cuboid like:
# 
# Surface Area: 600
# Volume: 1000

a = 10
b = 5
c = 8

surface = 2 * (a * b + b * c + a * c)
volume = a * b * c

print("Surface Area: " + str(surface))
print("Volume: " + str(volume))