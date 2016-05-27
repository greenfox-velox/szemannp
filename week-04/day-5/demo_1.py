from tkinter import *
from math import *

root = Tk()

size = 600

canvas = Canvas(root, width = size, height = size, bg = 'green')
canvas.pack()

def draw_triangle(x, y, size):
    canvas.create_polygon(x, y, x + size, y, x + size / 2, y + size * sqrt(3) / 2, fill = 'purple', outline = 'black')

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
