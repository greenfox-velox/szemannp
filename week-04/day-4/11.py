from tkinter import *

root = Tk()

size = 600

canvas = Canvas(root, width = size, height = size)
canvas.pack()

def recursive_drawing(size):
    offset = size // 9
    canvas.create_rectangle(offset + size // 3, offset, offset + size // 3 * 2, offset + size // 3)
    canvas.create_rectangle(offset, offset + size // 3, offset + size // 3, offset + size // 3 * 2)
    canvas.create_rectangle(offset + size // 3 * 2, offset + size // 3, offset + size, offset + size // 3 * 2)
    canvas.create_rectangle(offset + size // 3, offset + size // 3 * 2, offset + size // 3 * 2, offset + size)
    offset = (size // 3) ** 2
    if size <= 3:
        pass
    else:
        recursive_drawing(size // 3)
        recursive_drawing(size // 3 // 3)


recursive_drawing(600)
root.mainloop()


# canvas.create_line(float(size / 3), 0, float(size / 3), size)
# canvas.create_line(float(size / 3 * 2), 0, float(size / 3 * 2), size)
# canvas.create_line(0, float(size / 3), size, size, float(size / 3))
# canvas.create_line(0, float(size / 3 * 2), size, float(size / 3 * 2))
# size = float(size / 3)
# offset = float(size / 3)
