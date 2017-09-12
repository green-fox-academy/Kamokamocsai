# - Create a variable named `af`
#   with the following content: `[4, 5, 6, 7]`
# - Print all the elements of `af`

af = [4, 5, 6, 7]

def af_elements(numbers):
    for i in range(af[0:-1]):
        i = i + 1
        print(af[i])
    return
af_elements(af)