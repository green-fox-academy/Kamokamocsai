# Given a string, compute recursively a new string where all the 'x' chars have been removed.

def string_checker(string):
    if string == "":
        return ""
    elif string[0] == "x":
        return "" + string_checker(string[1:])
    else: 
        return string[0] + string_checker(string[1:])
        


print(string_checker("kmoegnjxnckjbisbcbccbcxxubix"))