class Garden(object):
    def __init__(self):
        self.flowers = []
        self.trees = []

    def add_flower(self, flower):
        self.flowers.append(flower)


    def add_tree(self, tree):
        self.trees.append(tree)


    def add_water(self, amount):
        self.water_needs = []
        for i in self.flowers:
            if i.status() == "Needs water!":
                self.water_needs.append(i)
        for i in self.trees:
            if i.status() == "Needs water!":
                self.water_needs.append(i)
        for i in self.water_needs:
            i.get_water(amount / len(self.water_needs()))        


class Flower(object):
    def __init__(self, color):
        self.color = color
        self.water_amount = 0

    def status(self):
        if self.water_amount < 5:
            return "Needs water!"
        else:
            return "Doesn't needs water!"


    def get_water(self, amount):
        self.water_amount += amount * 0.75


class Tree(object):
    def __init__(self, color):
        self.color = color
        self.water_amount = 0

    def status(self):
        if self.water_amount < 10:
            return "needs water!"
        else:
            return "doesn't needs water!"


    def get_water(self, amount):
        self.water_amount += amount * 0.4


flower1 = Flower("yellow")
Garden().add_flower("flower1")

print("The {} flower {}".format(self.color, self.status))