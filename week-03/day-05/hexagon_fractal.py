from tkinter import *
import math
import time

root = Tk()

canvas = Canvas(root, width='600', height='600')
canvas.pack()

size = 290


def draw_hexagon(x, y, size):
    height = math.sqrt(3) / 2 * size
    canvas.create_polygon(x, y, 
                          x + size / 2, y - height, 
                          x + size * 1.5, y - height, 
                          x + size * 2, y,
                          x + size * 1.5, y + height,
                          x + size / 2, y + height,
                          outline='black', fill='')




def draw_fractal(x, y, size):
    time.sleep(0.005)
    canvas.update()
    height = math.sqrt(3) / 2 * size
    if size < 5:
        return
    else:
        draw_hexagon(x, y, size)
        draw_fractal(x + size / 4, y - height / 2, size / 2)
        draw_fractal(x + size, y, size / 2)
        draw_fractal(x + size / 4, y + height / 2, size / 2)
    
draw_fractal(10, 300, 290)
root.mainloop()