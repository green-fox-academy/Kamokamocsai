# Create Sharpie class
# We should know about each sharpie their 
# color (which should be a string), 
# width (which will be a floating point number), 
# ink_amount (another floating point number).
# When creating one, we need to specify the color and the width
# Every sharpie is created with a default 100 as ink_amount
# We can use() the sharpie objects which decreases inkAmount.

class Sharpie(object):
    def __init__(self, color, width):
        self.color = color
        self.width = width
        self.ink_amount = 100

    def use(self):
        self.ink_amount -= 10

sharpie_blue = Sharpie("blue", 5)

print(sharpie_blue.color, sharpie_blue.width, sharpie_blue.ink_amount)

sharpie_blue.use()

print(sharpie_blue.ink_amount)