from tkinter import *
from math import *

root = Tk()

size = 600

canvas = Canvas(root, width = size, height = size, bg = 'green')
canvas.pack()

def draw_hexagon(x, y, size):
    canvas.create_polygon(x, y, x + size, y, x + size + size / 2 , y + size * sqrt(3) / 2, x + size, y + size * sqrt(3), x, y + size * sqrt(3), x - size / 2, y + size * sqrt(3) / 2, fill = 'orange', outline = 'black' )

def hex_factorial(x, y, size):
    draw_hexagon(x, y, size)
    if size <= 5:
        pass
    else:
        hex_factorial(x, y, size / 3)
        hex_factorial(x + size / 3 * 2, y, size / 3)
        hex_factorial(x + size, y + size * sqrt(3) / 3, size / 3)
        hex_factorial(x + size / 3 * 2, y + size * sqrt(3) / 2 + size / 3 * sqrt(3) / 2, size / 3)
        hex_factorial(x, y + size * sqrt(3) / 2 + size / 3 * sqrt(3) / 2, size / 3)
        hex_factorial(x - size / 3, y + size * sqrt(3) / 3, size / 3)

hex_factorial(200, 1, 200)

root.mainloop()
