# - Create a variable named `nimals`
#   with the following content: `["kuty", "macs", "cic"]`
# - Add all elements an `"a"` at the end

nimals = ["kuty", "macsk", "cic"]

def animals(list_of_animals):
    for i in range(len(list_of_animals)):
        list_of_animals[i] += "a"
    return list_of_animals

print(animals(nimals))