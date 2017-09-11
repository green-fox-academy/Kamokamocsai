current_hours = 14
current_minutes = 34
current_seconds = 42

# Write a program that prints the remaining seconds (as an integer) from a
# day if the current time is represented bt the variables

day = 24 * 60
print(int(day - (current_hours*120)+(current_minutes*60)+current_seconds))