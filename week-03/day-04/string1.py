# Given a string, compute recursively (no loops) a new string where all the
# lowercase 'x' chars have been changed to 'y' chars.

def string_checker(string):
    if string == "":
        return ""
    elif string[0] == "x":
        return "y" + string_checker(string[1:])
    else: 
        return string[0] + string_checker(string[1:])
        

print(string_checker("kmoegnjxnckjbisbcbccbcxxubix"))