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