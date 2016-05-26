

from tkinter import *

root = Tk()

canvas_size = 800
half = 400

canvas = Canvas(root, width = canvas_size, height = canvas_size)

canvas.pack()
color = 'green'
for i in range(0, half + 1, 10):
    canvas.create_line(i, half, half, half - i, fill = color)
    canvas.create_line(canvas_size - i, half, half, half - i, fill = color)
    canvas.create_line(i, half, half, half + i, fill = color)
    canvas.create_line(canvas_size - i, half, half, half + i, fill = color)

root.mainloop()
