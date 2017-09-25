# Create a PostIt class that has
# a background_color
# a text on it
# a text_color
# Create a few example post-it objects:
# an orange with blue text: "Idea 1"
# a pink with black text: "Awesome"
# a yellow with green text: "Superb!"

class PostIt(object):
    def __init__(self, background_color, text, text_color):
        self.background_color = background_color
        self.text = text
        self.text_color = text_color


post_it1 = PostIt("orange", "Idea 1", "blue")
post_it2 = PostIt("pink", "Awesome", "black")
post_it3 = PostIt("yellow", "Superb!", "green")



print(post_it1.background_color, post_it1.text, post_it1.text_color)
print(post_it2.background_color, post_it2.text, post_it2.text_color)
print(post_it3.background_color, post_it3.text, post_it3.text_color)
