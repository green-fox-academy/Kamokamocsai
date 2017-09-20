from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.


def draw_square(square_size, color):
    canvas.create_rectangle(150 - square_size, 150 - square_size, 150 + square_size, 150 + square_size, fill=color)
    
draw_square(150, 'red')
draw_square(125, 'orange')
draw_square(105, 'yellow')
draw_square(84, 'green')
draw_square(63, 'blue')
draw_square(42, 'indigo')
draw_square(21, 'violet')


root.mainloop()