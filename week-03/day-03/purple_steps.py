from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()


def draw_square(square_size):
    x_pos = 0
    y_pos = 0
    while x_pos <= 300:
        canvas.create_rectangle(x_pos + square_size, y_pos + square_size , x_pos + square_size * 2, y_pos + square_size * 2, fill='red')
        x_pos += square_size
        y_pos += square_size

draw_square(10)


root.mainloop()