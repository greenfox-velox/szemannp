# reproduce r3.png

from tkinter import *

root = Tk()

canvas_width = 300
canvas_height = 300
canvas = Canvas(root, width = canvas_width, height = canvas_height)

canvas.pack()

def draw_squares_diagonal(square_size):
    for i in range(1, 200, square_size):
         canvas.create_rectangle(i, i, i + square_size, i + square_size, fill = 'purple')

draw_squares_diagonal(10)

root.mainloop()
