from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw a red horizontal line to the canvas' middle.
# draw a green vertical line to the canvas' middle.

canvas.create_line(0, 150, 300, 150, fill='red')
canvas.create_line(150, 0, 150, 300, fill='green')


root.mainloop()