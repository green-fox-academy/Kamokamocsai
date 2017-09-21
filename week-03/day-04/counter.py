# Write a recursive function that takes one parameter: n and counts down from n.

def number(num):
    if num == 0:
        return num
    else:
        print(num)
        return number(num - 1)

number(5)