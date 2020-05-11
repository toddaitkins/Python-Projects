# This is an educational project by Todd Aitkins and is "Open Source" - 2020

# import the tkinter GUI functions
from tkinter import *

# import the time module
import time

tk = Tk()
tk.title("Worlds Greatest Chess Game!")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)

# define the drawing space
canvas = Canvas(tk, width=1000, height=1000)
canvas.pack()

# define all positions on the board and give the coordinates for the upper left corner of each space
posn_a1 = [0, 875]
posn_a2 = [0, 750]
posn_a3 = [0, 625]
posn_a4 = [0, 500]
posn_a5 = [0, 375]
posn_a6 = [0, 250]
posn_a7 = [0, 125]
posn_a8 = [0, 0]
posn_b1 = [125, 875]
posn_b2 = [125, 750]
posn_b3 = [125, 625]
posn_b4 = [125, 500]
posn_b5 = [125, 375]
posn_b6 = [125, 250]
posn_b7 = [125, 125]
posn_b8 = [125, 0]
posn_c1 = [250, 875]
posn_c2 = [250, 750]
posn_c3 = [250, 625]
posn_c4 = [250, 500]
posn_c5 = [250, 375]
posn_c6 = [250, 250]
posn_c7 = [250, 125]
posn_c8 = [250, 0]
posn_d1 = [375, 875]
posn_d2 = [375, 750]
posn_d3 = [375, 625]
posn_d4 = [375, 500]
posn_d5 = [375, 375]
posn_d6 = [375, 250]
posn_d7 = [375, 125]
posn_d8 = [375, 0]
posn_e1 = [500, 875]
posn_e2 = [500, 750]
posn_e3 = [500, 625]
posn_e4 = [500, 500]
posn_e5 = [500, 375]
posn_e6 = [500, 250]
posn_e7 = [500, 125]
posn_e8 = [500, 0]
posn_f1 = [625, 875]
posn_f2 = [625, 750]
posn_f3 = [625, 625]
posn_f4 = [625, 500]
posn_f5 = [625, 375]
posn_f6 = [625, 250]
posn_f7 = [625, 125]
posn_f8 = [625, 0]
posn_g1 = [750, 875]
posn_g2 = [750, 750]
posn_g3 = [750, 625]
posn_g4 = [750, 500]
posn_g5 = [750, 375]
posn_g6 = [750, 250]
posn_g7 = [750, 125]
posn_g8 = [750, 0]
posn_h1 = [875, 875]
posn_h2 = [875, 750]
posn_h3 = [875, 625]
posn_h4 = [875, 500]
posn_h5 = [875, 375]
posn_h6 = [875, 250]
posn_h7 = [875, 125]
posn_h8 = [875, 0]

# -Global variable definitions-
white_color = 'white'
black_color = 'black'
board_color = 'gray'
piece_fill_color_black = '#303030'
piece_fill_color_black_selected = 'green'
piece_fill_color_white = 'white'
piece_fill_color_white_selected = 'green'
is_selected_pos = False

canvas_list = []


class ChessPiece:
    pass


class Pawn(ChessPiece):
    def __init__(self, name, ref_num, color, pos, shapes, alive, is_selected):
        self.name = name
        self.ref_num = ref_num
        self.color = color
        self.pos = pos
        self.shapes = shapes
        self.alive = alive
        self.is_selected = is_selected

    # Draw the pawn
    def draw(self):
        if not self.alive:
            return
        # set colors for piece
        if (self.color == black_color) and (self.is_selected == True):
            fill_color = piece_fill_color_black_selected
        elif (self.color == black_color) and (self.is_selected == False):
            fill_color = piece_fill_color_black
        elif (self.color == white_color) and (self.is_selected == True):
            fill_color = piece_fill_color_white_selected
        else:
            fill_color = piece_fill_color_white
            # This draws the base
        Xtopleft = self.pos[0] + 20
        Ytopleft = self.pos[1] + 105
        Xbotright = self.pos[0] + 105
        Ybotright = self.pos[1] + 120
        self.base = canvas.create_rectangle(Xtopleft, Ytopleft, Xbotright, Ybotright, fill=fill_color)
        # This draws the collar below the round head
        Xtopleft = self.pos[0] + 40
        Ytopleft = self.pos[1] + 45
        Xbotright = self.pos[0] + 85
        Ybotright = self.pos[1] + 55
        self.collar = canvas.create_rectangle(Xtopleft, Ytopleft, Xbotright, Ybotright, fill=fill_color)
        # This is the round head of the piece
        Xtopleft = self.pos[0] + 50
        Ytopleft = self.pos[1] + 20
        Xbotright = self.pos[0] + 75
        Ybotright = self.pos[1] + 45
        self.head = canvas.create_oval(Xtopleft, Ytopleft, Xbotright, Ybotright, fill=fill_color)
        # This draws the polygon to represent the body
        Xpt1 = self.pos[0] + 50
        Ypt1 = self.pos[1] + 55
        Xpt2 = self.pos[0] + 75
        Ypt2 = self.pos[1] + 55
        Xpt3 = self.pos[0] + 85
        Ypt3 = self.pos[1] + 105
        Xpt4 = self.pos[0] + 40
        Ypt4 = self.pos[1] + 105
        self.body = canvas.create_polygon(Xpt1, Ypt1, Xpt2, Ypt2, Xpt3, Ypt3, Xpt4, Ypt4,
                                          fill=fill_color, outline="black")
        # Add everything to the canvas_list so it can be tracked more easily and removed during game loop drawing
        self.shapes = []  # Clear the list of previous shapes
        self.shapes.append(self.base)
        self.shapes.append(self.collar)
        self.shapes.append(self.head)
        self.shapes.append(self.body)
        canvas_list.append(self.shapes)


class Bishop(ChessPiece):
    def __init__(self, name, ref_num, color, pos, shapes, alive, is_selected):
        self.name = name
        self.ref_num = ref_num
        self.color = color
        self.pos = pos
        self.shapes = shapes
        self.alive = alive
        self.is_selected = is_selected

    def draw(self):
        if not self.alive:
            return
        # set colors for piece
        if (self.color == black_color) and (self.is_selected == True):
            fill_color = piece_fill_color_black_selected
        elif (self.color == black_color) and (self.is_selected == False):
            fill_color = piece_fill_color_black
        elif (self.color == white_color) and (self.is_selected == True):
            fill_color = piece_fill_color_white_selected
        else:
            fill_color = piece_fill_color_white
            # This draws the polygon to represent the body
        Xpt1 = self.pos[0] + 50
        Ypt1 = self.pos[1] + 49
        Xpt2 = self.pos[0] + 75
        Ypt2 = self.pos[1] + 49
        Xpt3 = self.pos[0] + 85
        Ypt3 = self.pos[1] + 105
        Xpt4 = self.pos[0] + 40
        Ypt4 = self.pos[1] + 105
        self.body = canvas.create_polygon(Xpt1, Ypt1, Xpt2, Ypt2, Xpt3, Ypt3, Xpt4, Ypt4,
                                          fill=fill_color, outline="black")
        # This is the round head of the piece
        Xtopleft = self.pos[0] + 50
        Ytopleft = self.pos[1] + 12
        Xbotright = self.pos[0] + 75
        Ybotright = self.pos[1] + 45
        self.head = canvas.create_oval(Xtopleft, Ytopleft, Xbotright, Ybotright, fill=fill_color)
        # This is the tiny round top of the head of the piece
        Xtopleft = self.pos[0] + 57
        Ytopleft = self.pos[1] + 5
        Xbotright = self.pos[0] + 68
        Ybotright = self.pos[1] + 15
        self.tiny_head = canvas.create_oval(Xtopleft, Ytopleft, Xbotright, Ybotright, fill=fill_color)
        # This draws the collar below the round head
        Xtopleft = self.pos[0] + 40
        Ytopleft = self.pos[1] + 39
        Xbotright = self.pos[0] + 85
        Ybotright = self.pos[1] + 49
        self.collar = canvas.create_rectangle(Xtopleft, Ytopleft, Xbotright, Ybotright, fill=fill_color)
        # This draws the base
        Xtopleft = self.pos[0] + 20
        Ytopleft = self.pos[1] + 105
        Xbotright = self.pos[0] + 105
        Ybotright = self.pos[1] + 120
        self.base = canvas.create_rectangle(Xtopleft, Ytopleft, Xbotright, Ybotright, fill=fill_color)
        # Add everything to the canvas_list so it can be tracked more easily and removed during game loop drawing
        self.shapes = []  # Clear the list of previous shapes
        self.shapes.append(self.base)
        self.shapes.append(self.collar)
        self.shapes.append(self.tiny_head)
        self.shapes.append(self.head)
        self.shapes.append(self.body)
        canvas_list.append(self.shapes)


class Rook(ChessPiece):
    def __init__(self, name, ref_num, color, pos, shapes, alive, is_selected):
        self.name = name
        self.ref_num = ref_num
        self.color = color
        self.pos = pos
        self.shapes = shapes
        self.alive = alive
        self.is_selected = is_selected

    def draw(self):
        if not self.alive:
            return
        # set colors for piece
        if (self.color == black_color) and (self.is_selected == True):
            fill_color = piece_fill_color_black_selected
        elif (self.color == black_color) and (self.is_selected == False):
            fill_color = piece_fill_color_black
        elif (self.color == white_color) and (self.is_selected == True):
            fill_color = piece_fill_color_white_selected
        else:
            fill_color = piece_fill_color_white
            # pos[] is the list containing the coordinates for the upper left corner of the square
        # This draws the polygon to represent the body
        Xpt1 = self.pos[0] + 50
        Ypt1 = self.pos[1] + 49
        Xpt2 = self.pos[0] + 75
        Ypt2 = self.pos[1] + 49
        Xpt3 = self.pos[0] + 85
        Ypt3 = self.pos[1] + 105
        Xpt4 = self.pos[0] + 40
        Ypt4 = self.pos[1] + 105
        self.body = canvas.create_polygon(Xpt1, Ypt1, Xpt2, Ypt2, Xpt3, Ypt3, Xpt4, Ypt4,
                                          fill=fill_color, outline="black")
        # This draws the polygon to represent the head of the piece
        Xpt1 = self.pos[0] + 36
        Ypt1 = self.pos[1] + 20
        Xpt2 = self.pos[0] + 40
        Ypt2 = self.pos[1] + 49
        Xpt3 = self.pos[0] + 85
        Ypt3 = self.pos[1] + 49
        Xpt4 = self.pos[0] + 89
        Ypt4 = self.pos[1] + 20
        Xpt5 = self.pos[0] + 79
        Ypt5 = self.pos[1] + 20
        Xpt6 = self.pos[0] + 79
        Ypt6 = self.pos[1] + 30
        Xpt7 = self.pos[0] + 68
        Ypt7 = self.pos[1] + 30
        Xpt8 = self.pos[0] + 68
        Ypt8 = self.pos[1] + 20
        Xpt9 = self.pos[0] + 57
        Ypt9 = self.pos[1] + 20
        Xpt10 = self.pos[0] + 57
        Ypt10 = self.pos[1] + 30
        Xpt11 = self.pos[0] + 46
        Ypt11 = self.pos[1] + 30
        Xpt12 = self.pos[0] + 46
        Ypt12 = self.pos[1] + 20
        self.head = canvas.create_polygon(Xpt1, Ypt1, Xpt2, Ypt2, Xpt3, Ypt3, Xpt4, Ypt4,
                                          Xpt5, Ypt5, Xpt6, Ypt6, Xpt7, Ypt7, Xpt8, Ypt8, Xpt9, Ypt9, Xpt10,
                                          Ypt10, Xpt11, Ypt11, Xpt12, Ypt12, fill=fill_color, outline="black")
        # This draws the base
        Xtopleft = self.pos[0] + 20
        Ytopleft = self.pos[1] + 105
        Xbotright = self.pos[0] + 105
        Ybotright = self.pos[1] + 120
        self.base = canvas.create_rectangle(Xtopleft, Ytopleft, Xbotright, Ybotright, fill=fill_color)
        # Add everything to the canvas_list so it can be tracked more easily and removed during game loop drawing
        self.shapes = []  # Clear the list of previous shapes
        self.shapes.append(self.base)
        self.shapes.append(self.head)
        self.shapes.append(self.body)
        canvas_list.append(self.shapes)


class Knight(ChessPiece):
    def __init__(self, name, ref_num, color, pos, shapes, alive, is_selected):
        self.name = name
        self.ref_num = ref_num
        self.color = color
        self.pos = pos
        self.shapes = shapes
        self.alive = alive
        self.is_selected = is_selected

    def draw(self):
        if self.alive == False:
            return
        # set colors for piece
        if (self.color == black_color) and (self.is_selected == True):
            fill_color = piece_fill_color_black_selected
        elif (self.color == black_color) and (self.is_selected == False):
            fill_color = piece_fill_color_black
        elif (self.color == white_color) and (self.is_selected == True):
            fill_color = piece_fill_color_white_selected
        else:
            fill_color = piece_fill_color_white
            # pos[] is the list containing the coordinates for the upper left corner of the square
        # This draws the polygon to represent the body
        Xpt1 = self.pos[0] + 30
        Ypt1 = self.pos[1] + 105
        Xpt2 = self.pos[0] + 95
        Ypt2 = self.pos[1] + 105
        Xpt3 = self.pos[0] + 75
        Ypt3 = self.pos[1] + 81
        Xpt4 = self.pos[0] + 75
        Ypt4 = self.pos[1] + 73
        Xpt5 = self.pos[0] + 85
        Ypt5 = self.pos[1] + 63
        Xpt6 = self.pos[0] + 85
        Ypt6 = self.pos[1] + 38
        Xpt7 = self.pos[0] + 70
        Ypt7 = self.pos[1] + 12
        Xpt8 = self.pos[0] + 58
        Ypt8 = self.pos[1] + 9
        Xpt9 = self.pos[0] + 58
        Ypt9 = self.pos[1] + 13
        Xpt10 = self.pos[0] + 48
        Ypt10 = self.pos[1] + 21
        Xpt11 = self.pos[0] + 45
        Ypt11 = self.pos[1] + 45
        Xpt12 = self.pos[0] + 33
        Ypt12 = self.pos[1] + 65
        Xpt13 = self.pos[0] + 40
        Ypt13 = self.pos[1] + 72
        Xpt14 = self.pos[0] + 51
        Ypt14 = self.pos[1] + 65
        Xpt15 = self.pos[0] + 55
        Ypt15 = self.pos[1] + 68
        Xpt16 = self.pos[0] + 52
        Ypt16 = self.pos[1] + 85
        self.body = canvas.create_polygon(Xpt1, Ypt1, Xpt2, Ypt2, Xpt3, Ypt3, Xpt4, Ypt4,
                                          Xpt5, Ypt5, Xpt6, Ypt6, Xpt7, Ypt7, Xpt8, Ypt8, Xpt9, Ypt9, Xpt10,
                                          Ypt10, Xpt11, Ypt11, Xpt12, Ypt12, Xpt13, Ypt13, Xpt14, Ypt14, Xpt15,
                                          Ypt15, Xpt16, Ypt16, fill=fill_color, outline="black")
        # This draws the base
        Xtopleft = self.pos[0] + 20
        Ytopleft = self.pos[1] + 105
        Xbotright = self.pos[0] + 105
        Ybotright = self.pos[1] + 120
        self.base = canvas.create_rectangle(Xtopleft, Ytopleft, Xbotright, Ybotright,
                                            fill=fill_color)
        # Add everything to the canvas_list so it can be tracked more easily and removed during game loop drawing
        self.shapes = []  # Clear the list of previous shapes
        self.shapes.append(self.base)
        self.shapes.append(self.body)
        canvas_list.append(self.shapes)


class Queen(ChessPiece):
    def __init__(self, name, ref_num, color, pos, shapes, alive, is_selected):
        self.name = name
        self.ref_num = ref_num
        self.color = color
        self.pos = pos
        self.shapes = shapes
        self.alive = alive
        self.is_selected = is_selected

    def draw(self):
        if self.alive == False:
            return
        # set colors for piece
        if (self.color == black_color) and (self.is_selected == True):
            fill_color = piece_fill_color_black_selected
        elif (self.color == black_color) and (self.is_selected == False):
            fill_color = piece_fill_color_black
        elif (self.color == white_color) and (self.is_selected == True):
            fill_color = piece_fill_color_white_selected
        else:
            fill_color = piece_fill_color_white
            # pos[] is the list containing the coordinates for the upper left corner of the square
        # This draws the polygon to represent the body
        Xpt1 = self.pos[0] + 50
        Ypt1 = self.pos[1] + 40
        Xpt2 = self.pos[0] + 75
        Ypt2 = self.pos[1] + 40
        Xpt3 = self.pos[0] + 85
        Ypt3 = self.pos[1] + 105
        Xpt4 = self.pos[0] + 40
        Ypt4 = self.pos[1] + 105
        self.body = canvas.create_polygon(Xpt1, Ypt1, Xpt2, Ypt2, Xpt3, Ypt3, Xpt4, Ypt4,
                                          fill=fill_color, outline="black")
        # This draws the polygon to represent the head of the piece
        Xpt1 = self.pos[0] + 30
        Ypt1 = self.pos[1] + 10
        Xpt2 = self.pos[0] + 40
        Ypt2 = self.pos[1] + 40
        Xpt3 = self.pos[0] + 85
        Ypt3 = self.pos[1] + 40
        Xpt4 = self.pos[0] + 95
        Ypt4 = self.pos[1] + 10
        Xpt5 = self.pos[0] + 85
        Ypt5 = self.pos[1] + 10
        Xpt6 = self.pos[0] + 80
        Ypt6 = self.pos[1] + 25
        Xpt7 = self.pos[0] + 76
        Ypt7 = self.pos[1] + 25
        Xpt8 = self.pos[0] + 79
        Ypt8 = self.pos[1] + 10
        Xpt9 = self.pos[0] + 73
        Ypt9 = self.pos[1] + 10
        Xpt10 = self.pos[0] + 71
        Ypt10 = self.pos[1] + 25
        Xpt11 = self.pos[0] + 65
        Ypt11 = self.pos[1] + 25
        Xpt12 = self.pos[0] + 66
        Ypt12 = self.pos[1] + 10
        Xpt13 = self.pos[0] + 59
        Ypt13 = self.pos[1] + 10
        Xpt14 = self.pos[0] + 60
        Ypt14 = self.pos[1] + 25
        Xpt15 = self.pos[0] + 54
        Ypt15 = self.pos[1] + 25
        Xpt16 = self.pos[0] + 52
        Ypt16 = self.pos[1] + 10
        Xpt17 = self.pos[0] + 46
        Ypt17 = self.pos[1] + 10
        Xpt18 = self.pos[0] + 49
        Ypt18 = self.pos[1] + 25
        Xpt19 = self.pos[0] + 45
        Ypt19 = self.pos[1] + 25
        Xpt20 = self.pos[0] + 40
        Ypt20 = self.pos[1] + 10
        self.head = canvas.create_polygon(Xpt1, Ypt1, Xpt2, Ypt2, Xpt3, Ypt3, Xpt4, Ypt4,
                                          Xpt5, Ypt5, Xpt6, Ypt6, Xpt7, Ypt7, Xpt8, Ypt8, Xpt9, Ypt9, Xpt10,
                                          Ypt10, Xpt11, Ypt11, Xpt12, Ypt12, Xpt13, Ypt13, Xpt14, Ypt14, Xpt15,
                                          Ypt15, Xpt16, Ypt16, Xpt17, Ypt17, Xpt18, Ypt18, Xpt19, Ypt19, Xpt20,
                                          Ypt20, fill=fill_color, outline="black")
        # This draws the base
        Xtopleft = self.pos[0] + 20
        Ytopleft = self.pos[1] + 105
        Xbotright = self.pos[0] + 105
        Ybotright = self.pos[1] + 120
        self.base = canvas.create_rectangle(Xtopleft, Ytopleft, Xbotright, Ybotright,
                                            fill=fill_color)
        # Add everything to the canvas_list so it can be tracked more easily and removed during game loop drawing
        self.shapes = []  # Clear the list of previous shapes
        self.shapes.append(self.base)
        self.shapes.append(self.head)
        self.shapes.append(self.body)
        canvas_list.append(self.shapes)


class King(ChessPiece):
    def __init__(self, name, ref_num, color, pos, shapes, alive, is_selected):
        self.name = name
        self.ref_num = ref_num
        self.color = color
        self.pos = pos
        self.shapes = shapes
        self.alive = alive
        self.is_selected = is_selected

    def draw(self):
        if self.alive == False:
            return
        # set colors for piece
        if (self.color == black_color) and (self.is_selected == True):
            fill_color = piece_fill_color_black_selected
        elif (self.color == black_color) and (self.is_selected == False):
            fill_color = piece_fill_color_black
        elif (self.color == white_color) and (self.is_selected == True):
            fill_color = piece_fill_color_white_selected
        else:
            fill_color = piece_fill_color_white
            # pos[] is the list containing the coordinates for the upper left corner of the square
        # This draws the polygon to represent the body
        Xpt1 = self.pos[0] + 50
        Ypt1 = self.pos[1] + 49
        Xpt2 = self.pos[0] + 75
        Ypt2 = self.pos[1] + 49
        Xpt3 = self.pos[0] + 85
        Ypt3 = self.pos[1] + 105
        Xpt4 = self.pos[0] + 40
        Ypt4 = self.pos[1] + 105
        self.body = canvas.create_polygon(Xpt1, Ypt1, Xpt2, Ypt2, Xpt3, Ypt3, Xpt4, Ypt4,
                                          fill=fill_color, outline="black")
        # This is the left part of the head of the piece
        Xtopleft = self.pos[0] + 45
        Ytopleft = self.pos[1] + 25
        Xbotright = self.pos[0] + 65
        Ybotright = self.pos[1] + 45
        self.left_head = canvas.create_oval(Xtopleft, Ytopleft, Xbotright, Ybotright, fill=fill_color)
        # This is the right part of the head of the piece
        Xtopleft = self.pos[0] + 60
        Ytopleft = self.pos[1] + 25
        Xbotright = self.pos[0] + 80
        Ybotright = self.pos[1] + 45
        self.right_head = canvas.create_oval(Xtopleft, Ytopleft, Xbotright, Ybotright, fill=fill_color)
        # This is the round head of the piece
        Xtopleft = self.pos[0] + 55
        Ytopleft = self.pos[1] + 18
        Xbotright = self.pos[0] + 70
        Ybotright = self.pos[1] + 45
        self.round_head = canvas.create_oval(Xtopleft, Ytopleft, Xbotright, Ybotright, fill=fill_color)
        # This is the tiny round top of the head of the piece
        Xtopleft = self.pos[0] + 57
        Ytopleft = self.pos[1] + 15
        Xbotright = self.pos[0] + 68
        Ybotright = self.pos[1] + 25
        self.tiny_head = canvas.create_oval(Xtopleft, Ytopleft, Xbotright, Ybotright, fill=fill_color)
        # This draws the collar below the round head
        Xtopleft = self.pos[0] + 40
        Ytopleft = self.pos[1] + 39
        Xbotright = self.pos[0] + 85
        Ybotright = self.pos[1] + 49
        self.collar = canvas.create_rectangle(Xtopleft, Ytopleft, Xbotright, Ybotright, fill=fill_color)
        # This draws the base
        Xtopleft = self.pos[0] + 20
        Ytopleft = self.pos[1] + 105
        Xbotright = self.pos[0] + 105
        Ybotright = self.pos[1] + 120
        self.base = canvas.create_rectangle(Xtopleft, Ytopleft, Xbotright, Ybotright, fill=fill_color)
        # This draws the vertical of the cross
        Xtopleft = self.pos[0] + 60
        Ytopleft = self.pos[1] + 3
        Xbotright = self.pos[0] + 65
        Ybotright = self.pos[1] + 17
        self.vert_cross = canvas.create_rectangle(Xtopleft, Ytopleft, Xbotright, Ybotright, fill=fill_color)
        # This draws the horizontal of the cross
        Xtopleft = self.pos[0] + 52
        Ytopleft = self.pos[1] + 7
        Xbotright = self.pos[0] + 73
        Ybotright = self.pos[1] + 11
        self.horz_cross = canvas.create_rectangle(Xtopleft, Ytopleft, Xbotright, Ybotright, fill=fill_color)
        # Add everything to the canvas_list so it can be tracked more easily and removed during game loop drawing
        self.shapes = []  # Clear the list of previous shapes
        self.shapes.append(self.horz_cross)
        self.shapes.append(self.vert_cross)
        self.shapes.append(self.base)
        self.shapes.append(self.collar)
        self.shapes.append(self.tiny_head)
        self.shapes.append(self.round_head)
        self.shapes.append(self.right_head)
        self.shapes.append(self.left_head)
        self.shapes.append(self.body)
        canvas_list.append(self.shapes)


class GameBoard:
    def __init__(self, canvas):
        global board_color
        self.canvas = canvas

    def draw(self):
        is_black_square = 1
        for row in range(0, 1000, 125):
            for column in range(0, 1000, 125):
                Xtopleft = column
                Ytopleft = row
                Xbotright = column + 125
                Ybotright = row + 125
                if (is_black_square % 2) == 0:
                    canvas.create_rectangle(Xtopleft, Ytopleft, Xbotright, Ybotright,
                                            fill=board_color)
                else:
                    pass
                is_black_square = is_black_square + 1
            is_black_square = is_black_square + 1


class Box:
    def __init__(self, canvas, pos, selected_piece, is_active_selection):
        self.canvas = canvas
        self.pos = pos
        self.selected_piece = selected_piece
        self.is_active_selection = is_active_selection

        # Create self.id for use later when drawing boxes - not sure if this is needed
        self.id = 0
        self.id2 = 0
        # Listen for the 'directional' keys to be pressed
        self.canvas.bind_all('<KeyPress-Up>', self.move_selection_box)
        self.canvas.bind_all('<KeyPress-Down>', self.move_selection_box)
        self.canvas.bind_all('<KeyPress-Left>', self.move_selection_box)
        self.canvas.bind_all('<KeyPress-Right>', self.move_selection_box)
        self.canvas.bind_all('<KeyPress-Return>', self.select_game_piece)

    def draw(self):
        box_color = 'red'
        Xtopleft_select = self.pos[0]
        Ytopleft_select = self.pos[1]
        Xbotright_select = self.pos[0] + 125
        Ybotright_select = self.pos[1] + 125
        self.id = canvas.create_rectangle(Xtopleft_select, Ytopleft_select,
                                          Xbotright_select, Ybotright_select, width=3, outline=box_color)
        canvas_list.append(self.id)
        if self.is_active_selection == True:
            box_color = 'yellow'
            Xtopleft_selected = self.pos[0] - 2
            Ytopleft_selected = self.pos[1] - 2
            Xbotright_selected = self.pos[0] + 127
            Ybotright_selected = self.pos[1] + 127
            self.id2 = canvas.create_rectangle(Xtopleft_selected, Ytopleft_selected,
                                               Xbotright_selected, Ybotright_selected, width=3, outline=box_color)
            canvas_list.append(self.id2)

    def exec_box_move(self, x, y):
        canvas.delete(self.id)  # Delete the old box
        self.pos[0] = self.pos[0] + x  # Change the  x position
        self.pos[1] = self.pos[1] + y  # Change the  y position
        self.draw()  # Draw new box

    def move_selection_box(self, event):
        if event.keysym == 'Up':
            if (self.pos[1] - 125) < 0:
                print("Selection box can't move UP any more, it's already on the top row!")
            else:
                self.exec_box_move(0, -125)
                print("Selection box moves UP. New position @ Column: {} Row: {}".format(self.pos[0], self.pos[1]))
        elif event.keysym == 'Down':
            if (self.pos[1] + 125) > 875:
                print("Selection box can't move DOWN any more, it's already on the bottom row!")
            else:
                self.exec_box_move(0, 125)
                print("Selection box moves DOWN. New position @ Column: {} Row: {}".format(self.pos[0], self.pos[1]))
        elif event.keysym == 'Left':
            if (self.pos[0] - 125) < 0:
                print("Selection box can't move LEFT any more, it's already on the furthest left column!")
            else:
                self.exec_box_move(-125, 0)
                print("Selection box moves LEFT. New position @ Column: {} Row: {}".format(self.pos[0], self.pos[1]))
        elif event.keysym == 'Right':
            if (self.pos[0] + 125) > 875:
                print("Selection box can't move RIGHT any more, it's already on the furthest right column!")
            else:
                self.exec_box_move(125, 0)
                print("Selection box moves RIGHT. New position @ Column: {} Row: {}".format(self.pos[0], self.pos[1]))
        else:
            pass

    def what_piece_on_square(self, square_ask):  # This method will return the object
        for i in range(len(game_play_info)):
            if square_ask == game_play_info[i].pos:
                # return the obj of the piece on square_ask
                print("Found piece on the square {}.  It's {}.".format(square_ask, game_play_info[i].name))
                return game_play_info[i]
        # no piece on square returns False
        print("There's no piece on square {}.".format(square_ask))
        return False

    def is_square_empty(self, square_ask):
        for i in range(len(game_play_info)):
            if square_ask == game_play_info[i].pos:
                # found a piece on the square, it's not empty, returning False
                print("Found piece on the square {}.  It's {}.".format(square_ask, game_play_info[i].name))
                return False
        # Didn't find any pieces on the square, it's empty, returning True
        print("There's no piece on square {}.".format(square_ask))
        return True

    def move_piece(self):
        for i in range(len(self.selected_piece.shapes)):  # Loop through the shapes drawn for selected piece
            canvas.delete(self.selected_piece.shapes[i])  # Delete each shape from the canvas for the selected piece
        self.selected_piece.pos = self.pos  # Change the piece's position
        self.selected_piece.draw()  # Draw the selected piece

    def select_game_piece(self, event):
        if self.is_active_selection:  # A piece is selected
            # There is an active selection - Check if the new (self.current_pos) square is empty
            if self.is_square_empty(self.pos):
                # This is a valid space to move (sorta - it's empty but isn't IAW rules of Chess)
                self.selected_piece.is_selected = False  # Deselect the piece
                print("Moving the selected piece to this new square.")
                self.move_piece()  # Move the piece
                self.is_active_selection = False  # Deselect box
            elif not self.is_square_empty(self.pos):
                # This is not a valid space to move since it's not empty
                print("You can't move the {} to the square at {}.  It's not empty.".format(self.selected_piece.name,
                                                                                           self.pos))
            else:
                # This case shouldn't be possible.
                print(
                    "Error #1:  Selection Box tried to select a new square and 'is_square_empty' wasn't True or False.")
        elif not self.is_active_selection:  # No piece has been selected
            # There is not an active selection - Check if the square is empty
            if self.is_square_empty(self.pos):
                # This is not a valid space to select since it's empty
                print("You can't select an empty square, there's no piece there to move silly.")
            elif not self.is_square_empty(self.pos):
                # This is a valid space to select since it's not empty and there's a piece on it
                # Update the selected_piece attribute with current_pos
                self.selected_piece = self.what_piece_on_square(self.pos)
                # Change the selected_piece is_selected to True
                self.what_piece_on_square(self.pos).is_selected = True
                print(
                    "You selected the {} which is currently positioned on the square at {}.".format(self.selected_piece,
                                                                                                    self.pos))
                # Change the is_active_selection to True for all objects in Class
                self.is_active_selection = True
            else:
                # This case shouldn't be possible.
                print("Error #2:  Selection Box tried something and it didn't work.")
        else:
            # This case shouldn't be possible.
            print("Error #3:  Selection Box tried to select a piece and 'Active Selection' wasn't True or False.")


# Create a gameboard object for playing on of Class GameBoard
gameboard = GameBoard(canvas)

# Create list for main game play info
game_play_info = [
    # All game pieces are created with their initial position (pos) set at normal game starting position
    # Format for args: name, ref_num, color, pos, alive

    # Create White Pawns as objects of Class Pawn
    Pawn("White Pawn One", 1, white_color, posn_a2, [], True, False),
    Pawn("White Pawn Two", 2, white_color, posn_b2, [], True, False),
    Pawn("White Pawn Three", 3, white_color, posn_c2, [], True, False),
    Pawn("White Pawn Four", 4, white_color, posn_d2, [], True, False),
    Pawn("White Pawn Five", 5, white_color, posn_e2, [], True, False),
    Pawn("White Pawn Six", 6, white_color, posn_f2, [], True, False),
    Pawn("White Pawn Seven", 7, white_color, posn_g2, [], True, False),
    Pawn("White Pawn Eight", 8, white_color, posn_h2, [], True, False),

    # Create Black Pawns as objects of Class Pawn
    Pawn("Black Pawn One", 9, black_color, posn_a7, [], True, False),
    Pawn("Black Pawn Two", 10, black_color, posn_b7, [], True, False),
    Pawn("Black Pawn Three", 11, black_color, posn_c7, [], True, False),
    Pawn("Black Pawn Four", 12, black_color, posn_d7, [], True, False),
    Pawn("Black Pawn Five", 13, black_color, posn_e7, [], True, False),
    Pawn("Black Pawn Six", 14, black_color, posn_f7, [], True, False),
    Pawn("Black Pawn Seven", 15, black_color, posn_g7, [], True, False),
    Pawn("Black Pawn Eight", 16, black_color, posn_h7, [], True, False),

    # Create Bishops as objects of Class Bishop
    Bishop("White Bishop One", 17, white_color, posn_c1, [], True, False),
    Bishop("White Bishop Two", 18, white_color, posn_f1, [], True, False),
    Bishop("Black Bishop One", 19, black_color, posn_c8, [], True, False),
    Bishop("Black Bishop Two", 20, black_color, posn_f8, [], True, False),

    # Create Rooks as objects of Class Rook
    Rook("White Rook One", 21, white_color, posn_a1, [], True, False),
    Rook("White Rook Two", 22, white_color, posn_h1, [], True, False),
    Rook("Black Rook One", 23, black_color, posn_a8, [], True, False),
    Rook("Black Rook Two", 24, black_color, posn_h8, [], True, False),

    # Create Knights as objects of Class Knight
    Knight("White Knight One", 25, white_color, posn_b1, [], True, False),
    Knight("White Knight Two", 26, white_color, posn_g1, [], True, False),
    Knight("Black Knight One", 27, black_color, posn_b8, [], True, False),
    Knight("Black Knight Two", 28, black_color, posn_g8, [], True, False),

    # Create Queens as objects of Class Queen
    Queen("White Queen", 29, white_color, posn_d1, [], True, False),
    Queen("Black Queen", 30, black_color, posn_d8, [], True, False),

    # Create Kings as objects of Class King
    King("White King", 31, white_color, posn_e1, [], True, False),
    King("Black King", 32, black_color, posn_e8, [], True, False)]

# Draw the gameboard
gameboard.draw()

# Create box for selecting a playing piece of Class Box - initial args are ambiguous and don't really matter
select = Box(canvas, posn_e4, game_play_info[0], False)

# Main program loop
while 1:
    # Clear the canvas of all objects drawn on the board (e.g. everything but gameboard) then clear the list for next cycle
    for i in range(len(canvas_list)):
        canvas.delete(canvas_list[i])
    canvas_list = []
    # Loop through game_play_info list and call each .draw method for all pieces/objects
    for i in range(len(game_play_info)):
        game_play_info[i].draw()

    select.draw()
    tk.update_idletasks()
    tk.update()
    # Create a time delay to slow main program loop (not sure if this is needed)
    time.sleep(0.01)
