from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# fill the canvas with a checkerboard pattern.

cell_size = 300 / 8

def draw_checkerboard():
    for row in range(8):             
        for column in range(8):           
            if (row + column) % 2 == 0:     
                canvas.create_rectangle(column * cell_size, row * cell_size, column * cell_size + cell_size, row * cell_size + cell_size, fill='black')

draw_checkerboard()

root.mainloop()