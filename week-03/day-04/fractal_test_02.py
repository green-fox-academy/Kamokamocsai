from tkinter import *
import math
root = Tk()

canvas_width = 600
canvas_height = 600
canvas = Canvas(root, width=canvas_width, height=canvas_height, bg="yellow")
canvas.pack()
width = canvas_width/3

def carpet(x,y,width):
    if width < 2:
        pass
    else:
        start_x = x + width
        start_y = y + width
        canvas.create_line(start_x,y,start_x,y+width*3)
        canvas.create_line(start_x+width,y,start_x+width,y+width*3)
        canvas.create_line(x,start_y,x+width*3,start_y)
        canvas.create_line(x,start_y+width,x+width*3,start_y+width)
        return carpet(start_x,y,width/3), carpet(x,start_y,width/3), carpet(start_x+width,start_y,width/3), carpet(start_x,start_y+width,width/3)

carpet(0,0,width)

root.mainloop()