def josephus(num):
    binary = bin(num)
    flag = True
    for i in range(2,len(binary)):
        if binary[i] == "1" and flag:
            highest_one_bit = len(binary) - i - 1
            flag = False
    value_of_l = num - 2**highest_one_bit
    safe_position = 2 * value_of_l  + 1
    return safe_position

print(josephus(int(input("How many: "))))