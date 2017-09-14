# Sort that list

# Create a function that takes a list of numbers as parameter
# Returns a list where the elements are sorted in ascending numerical order
# Make a second boolean parameter, if it's true sort that list descending
# Example

# input [34, 12, 24, 9, 5]
# output [5, 9, 12, 24, 34]

input_nums = [34, 12, 24, 9, 5]

def ascended_list(the_list):
    for numbers in range(len(the_list)-1,0,-1):
        for i in range(numbers):
            if the_list[i] > the_list[i+1]:
                the_list[i], the_list[i+1] = the_list[i+1], the_list[i]
    print(input_nums)
    
ascended_list(input_nums)