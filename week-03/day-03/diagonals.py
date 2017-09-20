from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw the canvas' diagonals in green.

canvas.create_line(0, 0, 310, 310, fill='red')
canvas.create_line(302, 0, 0, 302, fill='green')


root.mainloop()