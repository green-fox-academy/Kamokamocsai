# - Create a variable named `af`
#   with the following content: `[4, 5, 6, 7]`
# - Print all the elements of `af`

af = [4, 5, 6, 7]

def af_elements(numbers):
    for i in range(len(af[0:])):
        print(af[i])
        i = i + 1
    return
af_elements(af)