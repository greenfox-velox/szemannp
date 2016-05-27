from tkinter import *
from math import *
from random import randint

root = Tk()

size = 600

canvas = Canvas(root, width = size, height = size, bg = ('#' + '%06X' % randint(0, 0xFFFFFF)))
canvas.pack()

colors = []
fill_color = 0

def get_random_color_array(color_list_size):
    for i in range(color_list_size):
        colors.append('#' + '%06X' % randint(0, 0xFFFFFF))
    return colors

get_random_color_array(500)

def draw_triangle(x, y, size):
    fill_color = colors[randint(0, 99)]
    canvas.create_polygon(x, y, x + size, y, x + size / 2, y + size * sqrt(3) / 2, fill = fill_color, outline = 'black')

def fract_triangle(x, y, size):
    draw_triangle(x, y, size)
    if size <= 5:
        pass
    else:
        fract_triangle(x, y, size /2)
        fract_triangle(x + size / 2, y, size / 2)
        fract_triangle(x + size / 4, y + size / 4 * sqrt(3), size / 2)

fract_triangle(1, 1, 600)

root.mainloop()
