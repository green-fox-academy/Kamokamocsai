#Swap the values of the wariables
a = 123
b = 526

a = a + b
b = a - b
a = a - b

print(a)
print(b)

# Easier way to solve:
a, b = b, a

print(a, b)
