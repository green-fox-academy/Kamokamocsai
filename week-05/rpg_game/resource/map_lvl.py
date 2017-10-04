class Map():
    def __init__(self):
        self.map1 = [
            [1, 1, 1, 0, 1, 0, 1, 1, 1, 1],
            [1, 1, 1, 0, 1, 0, 1, 0, 0, 1],
            [1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
            [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 0, 0, 1, 0, 1],
            [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
            [1, 1, 1, 0, 1, 0, 0, 1, 1, 1]       
        ]

    def can_move(self, x, y):
        # return self.map1[y][x] == 1
        if x < 0 or x > 9:
            return False
        elif y < 0 or y > 9:
            return False
        elif self.map1[y][x] == 1:
            return True
        # else:
        #     return True
            


Map()