# create a 300x300 canvas.
# draw a green 10x10 square to its center.
from tkinter import *

root = Tk()

canvas_width = 300
canvas_height = 300
canvas = Canvas(root, width = canvas_width, height = canvas_height)

canvas.pack()

middle_green_box = canvas.create_rectangle(145, 145, 155, 155, fill = 'green')

root.mainloop()
