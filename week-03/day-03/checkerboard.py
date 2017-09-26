# fill the canvas with a checkerboard pattern.
from tkinter import *

root = Tk()

canvas = Canvas(root, width='600', height='600')
canvas.pack()

cell_size = 600 / 8

def draw_checkerboard():
    for row in range(8):             
        for column in range(8):           
            if (row + column) % 2 == 0:     
                canvas.create_rectangle(column * cell_size, row * cell_size, 
                                        column * cell_size + cell_size, 
                                        row * cell_size + cell_size, fill='black')

draw_checkerboard()

root.mainloop()