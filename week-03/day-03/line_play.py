from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/line-play/r1.png]

def line_drawer():
    for i in range(14):
        canvas.create_line(0 + i * 10, 0 + i * 10, 150, 150, fill='light sea green')
    return i

line_drawer()

root.mainloop()