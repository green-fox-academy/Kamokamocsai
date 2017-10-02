from tkinter import *

size = 600

root = Tk()
root.configure(background ='black')
canvas = Canvas(root, width=size, height=size,bg="yellow",bd=0)
canvas.pack()

class App:
    def __init__(self):
        self.rect = None

    def base_shape(self, x, y, size):
        self.rect = canvas.create_rectangle(x, y, x+size, y+size, fill = "black", width=0)

    def move(self, dx, dy):
        canvas.move(self.rect, dx, dy )

myApp = App()

myApp.base_shape(0, 0, 100)

def on_key_press(e):
    if ( e.keysym == 'Up' ):
        myApp.move(0,-10)
    elif( e.keysym == 'Down' ):
        myApp.move(0,10)

# Tell the canvas that we prepared a function that can deal with the key press events
root.bind("<KeyPress>", on_key_press)
canvas.pack()

# Select the canvas to be in focused so it actually recieves the key hittings
canvas.focus_set()

root.mainloop()