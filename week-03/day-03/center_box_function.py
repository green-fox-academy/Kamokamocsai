from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# draw 3 squares with that function.

def draw_square(square_size, color):
    canvas.create_rectangle(150 - square_size, 150 - square_size, 150 + square_size, 150 + square_size, fill=color)
    
draw_square(100, 'yellow')
draw_square(50, 'blue')
draw_square(25, 'red')

root.mainloop()