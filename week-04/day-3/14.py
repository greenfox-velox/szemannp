# checkerboard

from tkinter import *

root = Tk()

canvas_width = 400
canvas_height = 400
size = canvas_height // 8
canvas = Canvas(root, width = canvas_width, height = canvas_height)

canvas.pack()

for i in range(8):
    for j in range(8):
        x = i * size
        y = j * size
        color = 'white'
        if (i + j) % 2 == 0:
            color = 'black'
        canvas.create_rectangle(x, y, x + size, y + size, fill = color)


root.mainloop()
