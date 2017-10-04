from tkinter import *
from map_lvl import Map


size = 720

root = Tk()
root.configure(background ='black')
root.title("Wanderer - RPG Game by Kamo")
canvas = Canvas(root, width=size, height=size, bg="yellow", bd=0)
canvas.pack()



class App:
    def __init__(self):
        # self.rect = None
        self.floor = PhotoImage(file = "img/floor.png")
        self.wall = PhotoImage(file = "img/wall.png")
        self.map = Map()
        self.draw_map()


    def draw_map(self):
        cell_size = size / 10
        for row in range(len(self.map.map1)):
            for column in range(len(self.map.map1)):
                if self.map.map1[row][column] == 1:
                    cell = canvas.create_image(column * cell_size + 2, row * cell_size + 2, image = self.floor, anchor = 'nw')
                else:
                    canvas.create_image(column * cell_size + 2, row * cell_size + 2, image = self.wall, anchor = 'nw')
                    

class Hero(object):
    def __init__(self):
        self.hero_imgs = {
            "Down": PhotoImage(file = "img/hero-down.png"),
            "Left": PhotoImage(file = "img/hero-left.png"),
            "Right": PhotoImage(file = "img/hero-right.png"),
            "Up": PhotoImage(file = "img/hero-up.png")
        }
        self.current_pos_x = 0
        self.current_pos_y = 0

    def hero(self, x, y):
        self.rect = canvas.create_image(x, y, image = self.hero_imgs["Down"], anchor= 'nw')

    def move(self, dx, dy, direction):
        # canvas.move(self.rect, self.current_pos += map1[x][y])
        if app.map.can_move(self.current_pos_x + dx, self.current_pos_y + dy):
            self.current_pos_x += dx
            self.current_pos_y += dy
            canvas.move(self.rect, dx*72, dy*72)
            canvas.itemconfig(self.rect, image = self.hero_imgs[direction])
            


app = App()

hero = Hero()

hero.hero(0, 0)

def on_key_press(e):
    if ( e.keysym == 'Up' ):
        hero.move(0,-1, e.keysym)
    elif( e.keysym == 'Down' ):
        hero.move(0,1, e.keysym)
    elif( e.keysym == 'Left' ):
        hero.move(-1,0, e.keysym)
    elif( e.keysym == 'Right' ):
        hero.move(1,0, e.keysym)


# Tell the canvas that we prepared a function that can deal with the key press events
root.bind("<KeyPress>", on_key_press)
canvas.pack()

# Select the canvas to be in focused so it actually recieves the key hittings
canvas.focus_set()



root.mainloop()