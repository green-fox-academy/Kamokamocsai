from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# draw 3 lines with that function.

coord_x = 20
coord_y = 25

def line_drawing(coord_x, coord_y):
    line = canvas.create_line(coord_x, coord_y, 150, 150, fill='green')
    line_two = canvas.create_line(coord_x + 150, coord_y, 150, 150, fill='red')
    line_three = canvas.create_line(coord_x + 300, coord_y, 150, 150, fill='blue')
    return line 

line_drawing(coord_x, coord_y)

root.mainloop()