# This is an educational project by Todd Aitkins and is "Open Source" - 2020

# import the tkinter GUI functions
from tkinter import *
# import the numpy module as np to use sin() and cos() functions
import numpy as np

tk = Tk()
tk.title("Sine vs. Cosine")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)

# define the drawing space
canvas = Canvas(tk, width=1100, height=550)
canvas.pack()

# define position of the graph legend
y_legend = 525


class Grid:
    def __init__(self):
        y_axis = canvas.create_line(550, 0, 550, 500, width=2)
        x_axis = canvas.create_line(50, 250, 1050, 250, width=2)
        x = 100
        while x < 1050:
            canvas.create_line(x, 0, x, 500, width=1)
            canvas.create_text(x, 510, text=str(x - 550) + "°")
            x = x + 90
        y = 70
        while y < 500:
            canvas.create_line(50, y, 1050, y, width=1)
            y = y + 90
        canvas.create_text(1060, 250, text="X")
        canvas.create_text(549, 522, text="Y")


class Curve:
    def __init__(self, curve_type, curve_color, curve_coord=[]):
        self.type = curve_type
        self.curve_color = curve_color
        self.curve_coord = curve_coord
        if self.type == "sine":
            for x in range(50, 1050):
                y = np.sin((x - 550) / -90) * 180 + 250
                self.curve_coord.append((x, y))
        elif self.type == "cosine":
            self.curve_coord = []
            for x in range(50, 1050):
                y = np.cos((x - 550) / -90) * 180 + 250
                self.curve_coord.append((x, y))

    def draw(self):
        global y_legend
        canvas.create_line(self.curve_coord, fill=self.curve_color, width=2)
        canvas.create_text(900, y_legend, text=self.type + " is the " + self.curve_color + " curve")
        y_legend = y_legend + 10


my_grid = Grid()
my_sine = Curve("sine", "red")
my_cosine = Curve("cosine", "blue")

my_sine.draw()
my_cosine.draw()

# Adding a comment to test VCS - changed the comment
# Added another comment for testing commits from the command line
while 1:
    tk.update_idletasks()
    tk.update()
