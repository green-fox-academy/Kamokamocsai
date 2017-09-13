# When saving this quote a disk error has occured. Please fix it.
# Add "always takes longer than" between the words "It" and "you"

quote = "Hofstadter's Law: It you expect, even when you take into account Hofstadter's Law."
new_words = "always takes longer than"

splitted_quote = quote.split(" ")
index_quote = splitted_quote.index("you")
splitted_quote.insert(index_quote, new_words) 
solution = " ".join(splitted_quote)

print(solution)