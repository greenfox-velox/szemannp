# reproduce r4.png

from tkinter import *

root = Tk()

canvas_width = 300
canvas_height = 300
canvas = Canvas(root, width = canvas_width, height = canvas_height)

canvas.pack()

x = 0
y = 0
offset = 10

def draw_increasing_diagonal_squares(x, y):
    box = canvas.create_rectangle(x, x, y, y, fill="purple")

for i in range(7):
    draw_increasing_diagonal_squares(x, x + 10 * i)
    x = x + 10 * i

root.mainloop()
