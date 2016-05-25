# create a 300x300 canvas.
# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.

from tkinter import *
from random import randint
root = Tk()

canvas_width = 300
canvas_height = 300
canvas = Canvas(root, width = canvas_width, height = canvas_height)

canvas.pack()

colors = []
fill_color = 0

def get_random_color_array(color_list_size):
    for i in range(color_list_size):
        colors.append('#' + '%06X' % randint(0, 0xFFFFFF))
    return colors

def draw_square(a, fill_color):
    canvas.create_rectangle(canvas_width / 2 - a / 2, canvas_height / 2 - a / 2, canvas_width / 2 + a / 2, canvas_height / 2 + a / 2, fill = fill_color)

get_random_color_array(100)

for i in range(canvas_width, 5, -5):
    fill_color = colors[randint(0, 99)]
    draw_square(i, fill_color)

root.mainloop()
