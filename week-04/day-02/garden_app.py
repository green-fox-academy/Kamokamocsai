class Garden(object):
    def __init__(self):
        self.flowers = []
        self.trees = []
        

    def add_flower(self, flower):
        self.flowers.append(flower)
        print("The {} flower {}".format(flower.color, flower.status()))

    def add_tree(self, tree):
        self.trees.append(tree)
        print("The {} tree {}".format(tree.color, tree.status()))

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

    def preview(self):
        for i in self.flowers:
            print("The {} flower {}".format(i.color, i.status()))



class Flower(object):
    def __init__(self, color):
        self.color = color
        self.water_amount = 0
        # print("The {} flower {}".format(self.color, self.status()))

    def status(self):
        if self.water_amount < 5:
            return "needs water!"
        else:
            return "doesn't needs water!"


    def get_water(self, amount):
        self.water_amount += amount * 0.75

    

class Tree(object):
    def __init__(self, color):
        self.color = color
        self.water_amount = 0
        # print("The {} tree {}".format(self.color, self.status()))

    def status(self):
        if self.water_amount < 10:
            return "needs water!"
        else:
            return "doesn't needs water!"


    def get_water(self, amount):
        self.water_amount += amount * 0.4


flower1 = Flower("yellow")
flower2 = Flower("blue")
tree1 = Tree("purple")
tree2 = Tree("orange")
Garden().add_flower(flower1)
Garden().add_flower(flower2)
Garden().add_tree(tree1)
Garden().add_tree(tree2)

Garden().add_water(40)

