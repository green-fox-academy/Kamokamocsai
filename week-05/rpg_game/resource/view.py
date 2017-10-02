from tkinter import *
from map_lvl import map1


size = 720

root = Tk()
root.configure(background ='black')
root.title("Wanderer - RPG Game by Kamo")
canvas = Canvas(root, width=size, height=size, bg="yellow", bd=0)
canvas.pack()



class App:
    def __init__(self):
        self.rect = None
        # self.hero_img = PhotoImage(file = "img/hero-down.png")
        self.hero_down = PhotoImage(file = "img/hero-down.png")
        self.hero_left = PhotoImage(file = "img/hero-left.png")
        self.hero_right = PhotoImage(file = "img/hero-right.png")
        self.hero_up = PhotoImage(file = "img/hero-up.png")
        self.floor = PhotoImage(file = "img/floor.png")
        self.wall = PhotoImage(file = "img/wall.png")
        self.draw_map()

    def hero(self, x, y, hero_img):
        self.rect = canvas.create_image(x, y, image = hero_img, anchor= 'nw')


    def move(self, dx, dy):
        
        canvas.move(self.rect, dx, dy)

    def draw_map(self):
        cell_size = size / 10
        for row in range(len(map1)):             
            for column in range(len(map1)): 
                if map1[row][column] == 1:
                    cell = canvas.create_image(column * cell_size + 2, row * cell_size + 2, image = self.floor, anchor = 'nw')
                    
                else:
                    canvas.create_image(column * cell_size + 2, row * cell_size + 2, image = self.wall, anchor = 'nw')
                    



myApp = App()

myApp.hero(0, 0, myApp.hero_down)

def on_key_press(e):
    if ( e.keysym == 'Up' ):
        myApp.move(0,-72)
    elif( e.keysym == 'Down' ):
        myApp.move(0,72)
    elif( e.keysym == 'Left' ):
        myApp.move(-72,0)
    elif( e.keysym == 'Right' ):
        myApp.move(72,0)


# Tell the canvas that we prepared a function that can deal with the key press events
root.bind("<KeyPress>", on_key_press)
canvas.pack()

# Select the canvas to be in focused so it actually recieves the key hittings
canvas.focus_set()



root.mainloop()