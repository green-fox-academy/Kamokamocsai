from tkinter import *
from map_lvl import Map
import random


size = 720

root = Tk()
root.iconbitmap('r', 'img/sword_icon.ico')
root.configure(background ='black')
root.title("Wanderer - RPG Game by Kamo")
canvas = Canvas(root, width=size + 200, height=size, bg="white", bd=0)
canvas.pack()




class App:
    def __init__(self):
        # self.rect = None
        self.floor = PhotoImage(file = "img/sw-floor.png")
        self.wall = PhotoImage(file = "img/sw-wall.png")
        self.statusbar_img = PhotoImage(file = "img/space.png")
        self.map = Map()
        self.draw_map()
        self.draw_statusbar()

    def draw_map(self):
        cell_size = size / 10
        for row in range(len(self.map.map1)):
            for column in range(len(self.map.map1)):
                if self.map.map1[row][column] == 1:
                    cell = canvas.create_image(column * cell_size + 2, row * cell_size + 2, image = self.floor, anchor = 'nw')
                else:
                    canvas.create_image(column * cell_size + 2, row * cell_size + 2, image = self.wall, anchor = 'nw')

    def draw_statusbar(self):
        self.statusbar = canvas.create_image(size, 0, image = self.statusbar_img, anchor= 'nw')
        self.menu_text = canvas.create_text(750, 50, fill="yellow", font="Times 20 italic bold", anchor="nw",
                        text="WANDERER\n -------------\nRPG Game\n      by\n    Kamo")
        self.menu_text = canvas.create_text(750, 240, fill="yellow", font="Times 15 bold", anchor="nw",
                        text="HP: "+str(Hero().current_hp))
        self.menu_text = canvas.create_text(750, 260, fill="yellow", font="Times 15 bold", anchor="nw",
                text="Defence: "+str(Hero().current_dp))
        self.menu_text = canvas.create_text(750, 280, fill="yellow", font="Times 15 bold", anchor="nw",
                text="Strike point: "+str(Hero().current_sp))






class Entity(object):    
    def __init__(self):
        self.img = img

#     def move_entity(self):
#         if on_key_press('Up' or 'Down'):
#             self.current_pos_x += dx
#             self.current_pos_y += dy
#             canvas.move(self.rect, dx*72, dy*72)


class Skeleton(Entity):
    def __init__(self):
        self.img = PhotoImage(file = "img/yoda-down.png")
        self.x_pos = 0
        self.y_pos = 0

    def skeleton(self, x, y):
        skeletons = 0
        while skeletons <=5:
            if app.map.can_move(x, y):
                self.skeleton = canvas.create_image(x*72, y*72, image = self.img, anchor= 'nw')
            x = random.randint(1, 9)
            y = random.randint(1, 9)
            skeletons += 1
            x_pos = x
            y_pos = y
        
    def move_skeleton(self):
        if on_key_press(e) == 'Up':
            self.canvas.move(self.skeleton, self.x_pos*72 +1, self.y_pos*72+1)  



class Boss(Entity):
    def __init__(self):
        self.img = PhotoImage(file = "img/han_solo.png")
        self.x_pos = 0
        self.y_pos = 0

    def han_solo(self, x, y):
        if app.map.can_move(x, y):
            canvas.create_image(x*72, y*72, image = self.img, anchor= 'nw')
            x = random.randint(1, 9)
            y = random.randint(1, 9)
            x_pos = x
            y_pos = y
                            


class Hero(object):
    def __init__(self):
        self.hero_imgs = {
            "Down": PhotoImage(file = "img/stormtrooper-down.png"),
            "Left": PhotoImage(file = "img/stormtrooper-left.png"),
            "Right": PhotoImage(file = "img/stormtrooper-right.png"),
            "Up": PhotoImage(file = "img/stormtrooper-up.png")
        }
        self.current_pos_x = 0
        self.current_pos_y = 0
        self.current_hp = 100
        self.current_dp = 200
        self.current_sp = 100

    def hero(self, x, y):
        self.rect = canvas.create_image(x, y, image = self.hero_imgs["Down"], anchor= 'nw')

    def move(self, dx, dy, direction):
        canvas.itemconfig(self.rect, image = self.hero_imgs[direction])
        if app.map.can_move(self.current_pos_x + dx, self.current_pos_y + dy):
            self.current_pos_x += dx
            self.current_pos_y += dy
            canvas.move(self.rect, dx*72, dy*72)
            
    def attack(self, target):
        pass

app = App()


skeleton = Skeleton()
skeleton.skeleton(random.randint(1, 9), random.randint(1, 9))

boss1 = Boss()
boss1.han_solo(random.randint(1,9), random.randint(1,9))

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