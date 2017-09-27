from tree_and_flower import Tree, Flower

class Garden(object):
    def __init__(self):
        self.plants = []

    def add_plant(self, plant):
        self.plants.append(plant)

    def watering(self, amount):
        print("\nWatering with " + str(amount))
        needs_water = self.get_thirsty_plant_indicates()
        amount_to_a_plant = amount / len(needs_water)
        for i in needs_water:
            self.plants[i].watering(amount_to_a_plant)
        self.status()

    def get_thirsty_plant_indicates(self):
        thirsty_plant_indicates = []
        for i in range(len(self.plants)):
            if self.plants[i].is_need_water():
                thirsty_plant_indicates.append(i)
        return thirsty_plant_indicates

    def status(self):
        for plant in self.plants:
            plant.status()

my_garden = Garden()
# my_tree = Tree("red")
my_garden.add_plant(Flower("yellow"))
my_garden.add_plant(Flower("blue"))
my_garden.add_plant(Tree("purple"))
my_garden.add_plant(Tree("orange"))

print(my_garden.status())
my_garden.watering(40)
my_garden.watering(70)