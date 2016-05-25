# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# draw 3 lines with that function.

from tkinter import *

root = Tk()
canvas_width = 300
canvas_height = 300
canvas = Canvas(root, width = canvas_width, height = canvas_height)
canvas.pack()

def draw_line(x, y):
    canvas.create_line(x, y, canvas_width / 2, canvas_height / 2, fill = 'orange')

draw_line(4, 278)
draw_line(290, 290)
draw_line(176, 54)

root.mainloop()
