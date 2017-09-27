def letter_counter(word):
    output = {}
    for letter in word:
        if letter in output:
            output[letter] += 1
        else:
            output[letter] = 1
    return output