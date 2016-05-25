# create a 300x300 canvas.
# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# draw 3 squares with that function.

from tkinter import *

root = Tk()

canvas_width = 300
canvas_height = 300
canvas = Canvas(root, width = canvas_width, height = canvas_height)

canvas.pack()

def draw_square(a):
    canvas.create_rectangle(canvas_width / 2 - a / 2, canvas_height / 2 - a / 2, canvas_width / 2 + a / 2, canvas_height / 2 + a / 2)

draw_square(35)
draw_square(99)
draw_square(175)

root.mainloop()
