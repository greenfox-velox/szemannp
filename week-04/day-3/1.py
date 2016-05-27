# create a 300x300 black canvas.
# draw a red horizontal line to its middle.
# draw a green vertical line to its middle.

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300', bg='black')
canvas.pack()

red_horizontal_line = canvas.create_line(150, 0, 150, 300, fill = 'red')
green_vertical_line = canvas.create_line(0, 150, 300, 150, fill = 'green')

root.mainloop()