from tkinter import *
# import time

root = Tk()

base_size = 600

canvas = Canvas(root, width=base_size, height=base_size, bg="yellow")
canvas.pack()

def draw_square(x0,y0, width, filler=None):
    canvas.create_rectangle(x0, y0, x0 + width, y0 + width, fill=filler)


def four_square(size, pos_x=0, pos_y=0):
    if size < 5:
        return
    size = size / 3
    draw_square(x0=pos_x, y0=pos_y + size, width=size)
    draw_square(x0=pos_x + size, y0=pos_y, width=size)
    draw_square(x0=pos_x + 2 * size, y0=pos_y + size, width=size)
    draw_square(x0=pos_x + size, y0=pos_y + 2 * size, width=size)
    four_square(size, pos_x, pos_y + size)
    four_square(size, pos_x + size, pos_y)
    four_square(size, pos_x + 2 * size, pos_y + size)
    four_square(size, pos_x + size, pos_y + 2 * size)

four_square(base_size)
root.mainloop()