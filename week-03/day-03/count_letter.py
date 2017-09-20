# Csináljon egy dict.-t a beadott szó betűi alapján.
# Pl. bemenet az, hogy "alma", a kimenete: {"a": 2, "l": 1, "m": 1}

text = input("Take a word: ")

def count_letters(text):
    counted_letters = {}
    for letter in text:
        if letter in counted_letters:
            counted_letters[letter] += 1
        else:
            counted_letters[letter] = 1
    return counted_letters

print(count_letters(text))