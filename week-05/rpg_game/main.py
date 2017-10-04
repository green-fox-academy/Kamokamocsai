from resource import map_lvl

class GameProcess(object):

    def __init__(self):
        self.map_level = map_level
        self.running = running
        self.level = level
        self.entities = []
        self.hero = hero

    def keyboard_handler(self):
        pass
        # call_hero_move
        # call_all_entities



# from view import View
# from map import Map

# class Game:
#     def __init__(self):
#         self.mymap = Map()
#         self.myview = View()
#         self.myview.draw_map(self.mymap.tiles)
#         self.myview.draw_entity("down", 0, 0)
#         self.myview.display()

# game = Game()