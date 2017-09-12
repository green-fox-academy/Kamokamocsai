# - Create (dynamically) a two dimensional list
#   with the following matrix. Use a loop!
#
#   1 0 0 0
#   0 1 0 0
#   0 0 1 0
#   0 0 0 1
#
# - Print this two dimensional list to the output

matrix = [1, 0, 0, 0]

line = ""
for i in range(0,4):
    line=""
    for j in range(0,4):
        if i == j:
            line += "1"
        else:
             line +="0"
        line+=" "
    print(line)

# def matrix_list(num_list):
#     while i is not (4):
#     for i in range(matrix):
#         print(matrix)
#         matrix[i] = matrix[6]
#         matrix[i+1] = matrix[i]
#         matrix[6] = matrix[i]
#         i = i + 1
#     return num_list

# matrix_list(matrix)
