from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a 50 long horizontal line from that point.
# draw 3 lines with that function.

x_coord = 25
y_coord = 50

def starting_point(x_coord, y_coord):
    line = canvas.create_line(x_coord, y_coord, 300, y_coord, fill='green')
    return line

starting_point(x_coord, y_coord)

root.mainloop()