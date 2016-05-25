# create a 300x300 canvas.
# fill it with four different size and color rectangles.

from tkinter import *

root = Tk()

canvas_width = 300
canvas_height = 300
canvas = Canvas(root, width = canvas_width, height = canvas_height)

canvas.pack()

canvas.create_rectangle(23, 56, 145, 120, fill = 'green')
canvas.create_rectangle(120, 150, 156, 184, fill = 'red')
canvas.create_rectangle(156, 40, 205, 76, fill = 'orange')
canvas.create_rectangle(210, 171, 276, 199, fill = 'blue')

root.mainloop()
