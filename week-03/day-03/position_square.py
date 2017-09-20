from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a square drawing function that takes 2 parameters:
# the x and y coordinates of the square's top left corner
# and draws a 50x50 square from that point.
# draw 3 squares with that function.


def draw_square(x_coord, y_coord):
    canvas.create_rectangle(x_coord, y_coord, x_coord + 50, y_coord + 50, fill='tomato')


draw_square(20, 20)
draw_square(100, 100)
draw_square(200, 200)

root.mainloop()