def fibonacci(number):
    if number <= 1:
        return number
    else:
        return fibonacci(number-1) + fibonacci(number-2)