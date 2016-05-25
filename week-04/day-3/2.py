# create a 300x300 canvas.
# draw a box that has different colored lines on each edge.

from tkinter import *

root = Tk()
canvas_width = 300
canvas_height = 300
canvas = Canvas(root, width = canvas_width, height = canvas_height, bg='black')
canvas.pack()

box_top_edge = canvas.create_line(2, 2, canvas_width + 2, 2, fill = 'green', width = 2)
box_bottom_edge = canvas.create_line(2, canvas_height + 2, canvas_width + 2, canvas_height + 2, fill = 'red', width = 2)
box_left_edge = canvas.create_line(2, 2, 2, canvas_height + 2, fill = 'purple', width = 2)
box_right_edge = canvas.create_line(canvas_width + 2, 2, canvas_width + 2, canvas_height + 2, fill = 'orange', width = 2)

root.mainloop()
