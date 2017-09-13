
students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
]

# create a function that takes a list of students and prints:
# - Who has got more candies than 4 candies

# create a function that takes a list of students and prints: 
#  - how many candies they have on average

def more_candies(student_list):
    new_list = []
    for student in student_list:
        if student['candies'] > 4:
            new_list.append(student['name'])
    # print(str(new_list) + " have more than 4 candies.") VAGY:
    print(new_list)

more_candies(students)


def average_candies(student_list):
    # average_list = []
    average = 0
    for student in student_list:
        average += student['candies']
        full_average = average / len(student)
        # average_list.append(student['candies'])
    # print(average_list)
    print(full_average)

average_candies(students)