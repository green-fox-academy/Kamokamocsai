from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()


def draw_square(square_size):
    canvas.create_rectangle(0 + square_size, 0 + square_size, square_size, square_size, fill='red')
    
draw_square(10)


root.mainloop()