from tkinter import *
from random import randint

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw four different size and color rectangles.

def rectangles_drawer(x_coord, y_coord):
    canvas.create_rectangle(x_coord + randint(0, 300), y_coord + randint(0, 300), randint(0, 300), randint(0, 300), fill='lime green')
    canvas.create_rectangle(x_coord + randint(0, 300), y_coord + randint(0, 300), randint(0, 300), randint(0, 300), fill='blue')
    canvas.create_rectangle(x_coord + randint(0, 300), y_coord + randint(0, 300), randint(0, 300), randint(0, 300), fill='red')
    canvas.create_rectangle(x_coord + randint(0, 300), y_coord + randint(0, 300), randint(0, 300), randint(0, 300), fill='purple')
    
rectangles_drawer(randint(0, 300), randint(0, 300))

root.mainloop()