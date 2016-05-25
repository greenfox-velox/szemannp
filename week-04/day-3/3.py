# create a 300x300 canvas.
# draw its diagonals in green.
from tkinter import *

root = Tk()

canvas_width = 300
canvas_height = 300
canvas = Canvas(root, width = canvas_width, height = canvas_height)

canvas.pack()

diagonal_1 = canvas.create_line(0, 0, canvas_width, canvas_height, fill = 'green', width = 2)
diagonal_1 = canvas.create_line(canvas_width, 0, 0, canvas_height, fill = 'green', width = 2)

root.mainloop()
