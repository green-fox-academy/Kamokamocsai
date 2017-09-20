from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw a box that has different colored lines on each edge.

canvas.create_line(0, 2, 300, 2, fill='red')
canvas.create_line(2, 0, 2, 300, fill='green')
canvas.create_line(0, 300, 300, 300, fill='blue')
canvas.create_line(300, 300, 300, 0, fill='yellow')

root.mainloop()