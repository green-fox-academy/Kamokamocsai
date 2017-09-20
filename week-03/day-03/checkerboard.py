from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# fill the canvas with a checkerboard pattern.

# offset_x = 10      
# offset_y = 10      
# cell_size = 10     

def draw_checkerboard():
    for row in range(6):             
        for column in range(6):           
            # if (row + column) % 2 == 0:     
            canvas.create_rectangle(column * 60, row, column + 60, row + 60)
                # color = 'white'
            # else:
            #     pass
                # color = 'black'
            # canvas.setFill(color)
            # canvas.drawRect(offset_x + row * cell_size, offset_y + column * cell_size, cell_size, cell_size)



draw_checkerboard()

root.mainloop()