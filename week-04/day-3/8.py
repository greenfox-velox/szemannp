# create a 300x300 canvas.
# create a square drawing function that takes 2 parameters:
# the x and y coordinates of the square's top left corner
# and draws a 50x50 square from that point.
# draw 3 squares with that function.

from tkinter import *

root = Tk()

canvas_width = 300
canvas_height = 300
canvas = Canvas(root, width = canvas_width, height = canvas_height)

canvas.pack()

def draw_squares(x, y):
    canvas.create_rectangle(x, y, x + 50, y + 50, fill = 'red')

draw_squares(20, 40)
draw_squares(123, 133)
draw_squares(201, 199)




root.mainloop()
