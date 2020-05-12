# This is an educational project "Chessboard" by Todd Aitkins and is "Open Source" - 2020

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
position_a1 = [0, 875]
position_a2 = [0, 750]
position_a3 = [0, 625]
position_a4 = [0, 500]
position_a5 = [0, 375]
position_a6 = [0, 250]
position_a7 = [0, 125]
position_a8 = [0, 0]
position_b1 = [125, 875]
position_b2 = [125, 750]
position_b3 = [125, 625]
position_b4 = [125, 500]
position_b5 = [125, 375]
position_b6 = [125, 250]
position_b7 = [125, 125]
position_b8 = [125, 0]
position_c1 = [250, 875]
position_c2 = [250, 750]
position_c3 = [250, 625]
position_c4 = [250, 500]
position_c5 = [250, 375]
position_c6 = [250, 250]
position_c7 = [250, 125]
position_c8 = [250, 0]
position_d1 = [375, 875]
position_d2 = [375, 750]
position_d3 = [375, 625]
position_d4 = [375, 500]
position_d5 = [375, 375]
position_d6 = [375, 250]
position_d7 = [375, 125]
position_d8 = [375, 0]
position_e1 = [500, 875]
position_e2 = [500, 750]
position_e3 = [500, 625]
position_e4 = [500, 500]
position_e5 = [500, 375]
position_e6 = [500, 250]
position_e7 = [500, 125]
position_e8 = [500, 0]
position_f1 = [625, 875]
position_f2 = [625, 750]
position_f3 = [625, 625]
position_f4 = [625, 500]
position_f5 = [625, 375]
position_f6 = [625, 250]
position_f7 = [625, 125]
position_f8 = [625, 0]
position_g1 = [750, 875]
position_g2 = [750, 750]
position_g3 = [750, 625]
position_g4 = [750, 500]
position_g5 = [750, 375]
position_g6 = [750, 250]
position_g7 = [750, 125]
position_g8 = [750, 0]
position_h1 = [875, 875]
position_h2 = [875, 750]
position_h3 = [875, 625]
position_h4 = [875, 500]
position_h5 = [875, 375]
position_h6 = [875, 250]
position_h7 = [875, 125]
position_h8 = [875, 0]

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
        self.base = None
        self.collar = None
        self.head = None
        self.body = None

    # Draw the pawn
    def draw(self):
        if not self.alive:
            return
        # set colors for piece
        if (self.color == black_color) and (self.is_selected is True):
            fill_color = piece_fill_color_black_selected
        elif (self.color == black_color) and (self.is_selected is False):
            fill_color = piece_fill_color_black
        elif (self.color == white_color) and (self.is_selected is True):
            fill_color = piece_fill_color_white_selected
        else:
            fill_color = piece_fill_color_white
            # This draws the base
        x_top_left = self.pos[0] + 20
        y_top_left = self.pos[1] + 105
        x_bot_right = self.pos[0] + 105
        y_bot_right = self.pos[1] + 120
        self.base = canvas.create_rectangle(x_top_left, y_top_left, x_bot_right, y_bot_right, fill=fill_color)
        # This draws the collar below the round head
        x_top_left = self.pos[0] + 40
        y_top_left = self.pos[1] + 45
        x_bot_right = self.pos[0] + 85
        y_bot_right = self.pos[1] + 55
        self.collar = canvas.create_rectangle(x_top_left, y_top_left, x_bot_right, y_bot_right, fill=fill_color)
        # This is the round head of the piece
        x_top_left = self.pos[0] + 50
        y_top_left = self.pos[1] + 20
        x_bot_right = self.pos[0] + 75
        y_bot_right = self.pos[1] + 45
        self.head = canvas.create_oval(x_top_left, y_top_left, x_bot_right, y_bot_right, fill=fill_color)
        # This draws the polygon to represent the body
        x_point_1 = self.pos[0] + 50
        y_point_1 = self.pos[1] + 55
        x_point_2 = self.pos[0] + 75
        y_point_2 = self.pos[1] + 55
        x_point_3 = self.pos[0] + 85
        y_point_3 = self.pos[1] + 105
        x_point_4 = self.pos[0] + 40
        y_point_4 = self.pos[1] + 105
        self.body = canvas.create_polygon(x_point_1, y_point_1, x_point_2, y_point_2, x_point_3, y_point_3, x_point_4,
                                          y_point_4,
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
        self.base = None
        self.collar = None
        self.tiny_head = None
        self.head = None
        self.body = None

    def draw(self):
        if not self.alive:
            return
        # set colors for piece
        if (self.color == black_color) and (self.is_selected is True):
            fill_color = piece_fill_color_black_selected
        elif (self.color == black_color) and (self.is_selected is False):
            fill_color = piece_fill_color_black
        elif (self.color == white_color) and (self.is_selected is True):
            fill_color = piece_fill_color_white_selected
        else:
            fill_color = piece_fill_color_white
            # This draws the polygon to represent the body
        x_point_1 = self.pos[0] + 50
        y_point_1 = self.pos[1] + 49
        x_point_2 = self.pos[0] + 75
        y_point_2 = self.pos[1] + 49
        x_point_3 = self.pos[0] + 85
        y_point_3 = self.pos[1] + 105
        x_point_4 = self.pos[0] + 40
        y_point_4 = self.pos[1] + 105
        self.body = canvas.create_polygon(x_point_1, y_point_1, x_point_2, y_point_2, x_point_3, y_point_3, x_point_4,
                                          y_point_4,
                                          fill=fill_color, outline="black")
        # This is the round head of the piece
        x_top_left = self.pos[0] + 50
        y_top_left = self.pos[1] + 12
        x_bot_right = self.pos[0] + 75
        y_bot_right = self.pos[1] + 45
        self.head = canvas.create_oval(x_top_left, y_top_left, x_bot_right, y_bot_right, fill=fill_color)
        # This is the tiny round top of the head of the piece
        x_top_left = self.pos[0] + 57
        y_top_left = self.pos[1] + 5
        x_bot_right = self.pos[0] + 68
        y_bot_right = self.pos[1] + 15
        self.tiny_head = canvas.create_oval(x_top_left, y_top_left, x_bot_right, y_bot_right, fill=fill_color)
        # This draws the collar below the round head
        x_top_left = self.pos[0] + 40
        y_top_left = self.pos[1] + 39
        x_bot_right = self.pos[0] + 85
        y_bot_right = self.pos[1] + 49
        self.collar = canvas.create_rectangle(x_top_left, y_top_left, x_bot_right, y_bot_right, fill=fill_color)
        # This draws the base
        x_top_left = self.pos[0] + 20
        y_top_left = self.pos[1] + 105
        x_bot_right = self.pos[0] + 105
        y_bot_right = self.pos[1] + 120
        self.base = canvas.create_rectangle(x_top_left, y_top_left, x_bot_right, y_bot_right, fill=fill_color)
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
        self.base = None
        self.head = None
        self.body = None

    def draw(self):
        if not self.alive:
            return
        # set colors for piece
        if (self.color == black_color) and (self.is_selected is True):
            fill_color = piece_fill_color_black_selected
        elif (self.color == black_color) and (self.is_selected is False):
            fill_color = piece_fill_color_black
        elif (self.color == white_color) and (self.is_selected is True):
            fill_color = piece_fill_color_white_selected
        else:
            fill_color = piece_fill_color_white
        # This draws the polygon to represent the body
        x_point_1 = self.pos[0] + 50
        y_point_1 = self.pos[1] + 49
        x_point_2 = self.pos[0] + 75
        y_point_2 = self.pos[1] + 49
        x_point_3 = self.pos[0] + 85
        y_point_3 = self.pos[1] + 105
        x_point_4 = self.pos[0] + 40
        y_point_4 = self.pos[1] + 105
        self.body = canvas.create_polygon(x_point_1, y_point_1, x_point_2, y_point_2, x_point_3, y_point_3, x_point_4,
                                          y_point_4, fill=fill_color, outline="black")
        # This draws the polygon to represent the head of the piece
        x_point_1 = self.pos[0] + 36
        y_point_1 = self.pos[1] + 20
        x_point_2 = self.pos[0] + 40
        y_point_2 = self.pos[1] + 49
        x_point_3 = self.pos[0] + 85
        y_point_3 = self.pos[1] + 49
        x_point_4 = self.pos[0] + 89
        y_point_4 = self.pos[1] + 20
        x_point_5 = self.pos[0] + 79
        y_point_5 = self.pos[1] + 20
        x_point_6 = self.pos[0] + 79
        y_point_6 = self.pos[1] + 30
        x_point_7 = self.pos[0] + 68
        y_point_7 = self.pos[1] + 30
        x_point_8 = self.pos[0] + 68
        y_point_8 = self.pos[1] + 20
        x_point_9 = self.pos[0] + 57
        y_point_9 = self.pos[1] + 20
        x_point_10 = self.pos[0] + 57
        y_point_10 = self.pos[1] + 30
        x_point_11 = self.pos[0] + 46
        y_point_11 = self.pos[1] + 30
        x_point_12 = self.pos[0] + 46
        y_point_12 = self.pos[1] + 20
        self.head = canvas.create_polygon(x_point_1, y_point_1, x_point_2, y_point_2, x_point_3, y_point_3, x_point_4,
                                          y_point_4, x_point_5, y_point_5, x_point_6, y_point_6, x_point_7, y_point_7,
                                          x_point_8, y_point_8, x_point_9, y_point_9, x_point_10, y_point_10,
                                          x_point_11, y_point_11, x_point_12, y_point_12, fill=fill_color,
                                          outline="black")
        # This draws the base
        x_top_left = self.pos[0] + 20
        y_top_left = self.pos[1] + 105
        x_bot_right = self.pos[0] + 105
        y_bot_right = self.pos[1] + 120
        self.base = canvas.create_rectangle(x_top_left, y_top_left, x_bot_right, y_bot_right, fill=fill_color)
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
        self.base = None
        self.body = None

    def draw(self):
        if not self.alive:
            return
        # set colors for piece
        if (self.color == black_color) and (self.is_selected is True):
            fill_color = piece_fill_color_black_selected
        elif (self.color == black_color) and (self.is_selected is False):
            fill_color = piece_fill_color_black
        elif (self.color == white_color) and (self.is_selected is True):
            fill_color = piece_fill_color_white_selected
        else:
            fill_color = piece_fill_color_white
            # pos[] is the list containing the coordinates for the upper left corner of the square
        # This draws the polygon to represent the body
        x_point_1 = self.pos[0] + 30
        y_point_1 = self.pos[1] + 105
        x_point_2 = self.pos[0] + 95
        y_point_2 = self.pos[1] + 105
        x_point_3 = self.pos[0] + 75
        y_point_3 = self.pos[1] + 81
        x_point_4 = self.pos[0] + 75
        y_point_4 = self.pos[1] + 73
        x_point_5 = self.pos[0] + 85
        y_point_5 = self.pos[1] + 63
        x_point_6 = self.pos[0] + 85
        y_point_6 = self.pos[1] + 38
        x_point_7 = self.pos[0] + 70
        y_point_7 = self.pos[1] + 12
        x_point_8 = self.pos[0] + 58
        y_point_8 = self.pos[1] + 9
        x_point_9 = self.pos[0] + 58
        y_point_9 = self.pos[1] + 13
        x_point_10 = self.pos[0] + 48
        y_point_10 = self.pos[1] + 21
        x_point_11 = self.pos[0] + 45
        y_point_11 = self.pos[1] + 45
        x_point_12 = self.pos[0] + 33
        y_point_12 = self.pos[1] + 65
        x_point_13 = self.pos[0] + 40
        y_point_13 = self.pos[1] + 72
        x_point_14 = self.pos[0] + 51
        y_point_14 = self.pos[1] + 65
        x_point_15 = self.pos[0] + 55
        y_point_15 = self.pos[1] + 68
        x_point_16 = self.pos[0] + 52
        y_point_16 = self.pos[1] + 85
        self.body = canvas.create_polygon(x_point_1, y_point_1, x_point_2, y_point_2, x_point_3, y_point_3, x_point_4,
                                          y_point_4, x_point_5, y_point_5, x_point_6, y_point_6, x_point_7, y_point_7,
                                          x_point_8, y_point_8, x_point_9, y_point_9, x_point_10, y_point_10,
                                          x_point_11, y_point_11, x_point_12, y_point_12, x_point_13, y_point_13,
                                          x_point_14, y_point_14, x_point_15, y_point_15, x_point_16, y_point_16,
                                          fill=fill_color, outline="black")
        # This draws the base
        x_top_left = self.pos[0] + 20
        y_top_left = self.pos[1] + 105
        x_bot_right = self.pos[0] + 105
        y_bot_right = self.pos[1] + 120
        self.base = canvas.create_rectangle(x_top_left, y_top_left, x_bot_right, y_bot_right, fill=fill_color)
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
        self.base = None
        self.head = None
        self.body = None

    def draw(self):
        if not self.alive:
            return
        # set colors for piece
        if (self.color == black_color) and (self.is_selected is True):
            fill_color = piece_fill_color_black_selected
        elif (self.color == black_color) and (self.is_selected is False):
            fill_color = piece_fill_color_black
        elif (self.color == white_color) and (self.is_selected is True):
            fill_color = piece_fill_color_white_selected
        else:
            fill_color = piece_fill_color_white
            # pos[] is the list containing the coordinates for the upper left corner of the square
        # This draws the polygon to represent the body
        x_point_1 = self.pos[0] + 50
        y_point_1 = self.pos[1] + 40
        x_point_2 = self.pos[0] + 75
        y_point_2 = self.pos[1] + 40
        x_point_3 = self.pos[0] + 85
        y_point_3 = self.pos[1] + 105
        x_point_4 = self.pos[0] + 40
        y_point_4 = self.pos[1] + 105
        self.body = canvas.create_polygon(x_point_1, y_point_1, x_point_2, y_point_2, x_point_3, y_point_3, x_point_4,
                                          y_point_4,
                                          fill=fill_color, outline="black")
        # This draws the polygon to represent the head of the piece
        x_point_1 = self.pos[0] + 30
        y_point_1 = self.pos[1] + 10
        x_point_2 = self.pos[0] + 40
        y_point_2 = self.pos[1] + 40
        x_point_3 = self.pos[0] + 85
        y_point_3 = self.pos[1] + 40
        x_point_4 = self.pos[0] + 95
        y_point_4 = self.pos[1] + 10
        x_point_5 = self.pos[0] + 85
        y_point_5 = self.pos[1] + 10
        x_point_6 = self.pos[0] + 80
        y_point_6 = self.pos[1] + 25
        x_point_7 = self.pos[0] + 76
        y_point_7 = self.pos[1] + 25
        x_point_8 = self.pos[0] + 79
        y_point_8 = self.pos[1] + 10
        x_point_9 = self.pos[0] + 73
        y_point_9 = self.pos[1] + 10
        x_point_10 = self.pos[0] + 71
        y_point_10 = self.pos[1] + 25
        x_point_11 = self.pos[0] + 65
        y_point_11 = self.pos[1] + 25
        x_point_12 = self.pos[0] + 66
        y_point_12 = self.pos[1] + 10
        x_point_13 = self.pos[0] + 59
        y_point_13 = self.pos[1] + 10
        x_point_14 = self.pos[0] + 60
        y_point_14 = self.pos[1] + 25
        x_point_15 = self.pos[0] + 54
        y_point_15 = self.pos[1] + 25
        x_point_16 = self.pos[0] + 52
        y_point_16 = self.pos[1] + 10
        x_point_17 = self.pos[0] + 46
        y_point_17 = self.pos[1] + 10
        x_point_18 = self.pos[0] + 49
        y_point_18 = self.pos[1] + 25
        x_point_19 = self.pos[0] + 45
        y_point_19 = self.pos[1] + 25
        x_point_20 = self.pos[0] + 40
        y_point_20 = self.pos[1] + 10
        self.head = canvas.create_polygon(x_point_1, y_point_1, x_point_2, y_point_2, x_point_3, y_point_3, x_point_4,
                                          y_point_4, x_point_5, y_point_5, x_point_6, y_point_6, x_point_7, y_point_7,
                                          x_point_8, y_point_8, x_point_9, y_point_9, x_point_10, y_point_10,
                                          x_point_11, y_point_11, x_point_12, y_point_12, x_point_13, y_point_13,
                                          x_point_14, y_point_14, x_point_15, y_point_15, x_point_16, y_point_16,
                                          x_point_17, y_point_17, x_point_18, y_point_18, x_point_19, y_point_19,
                                          x_point_20, y_point_20, fill=fill_color, outline="black")
        # This draws the base
        x_top_left = self.pos[0] + 20
        y_top_left = self.pos[1] + 105
        x_bot_right = self.pos[0] + 105
        y_bot_right = self.pos[1] + 120
        self.base = canvas.create_rectangle(x_top_left, y_top_left, x_bot_right, y_bot_right,
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
        self.horizontal_cross = None
        self.vertical_cross = None
        self.base = None
        self.collar = None
        self.tiny_head = None
        self.round_head = None
        self.right_head = None
        self.left_head = None
        self.body = None

    def draw(self):
        if not self.alive:
            return
        # set colors for piece
        if (self.color == black_color) and (self.is_selected is True):
            fill_color = piece_fill_color_black_selected
        elif (self.color == black_color) and (self.is_selected is False):
            fill_color = piece_fill_color_black
        elif (self.color == white_color) and (self.is_selected is True):
            fill_color = piece_fill_color_white_selected
        else:
            fill_color = piece_fill_color_white
            # pos[] is the list containing the coordinates for the upper left corner of the square
        # This draws the polygon to represent the body
        x_point_1 = self.pos[0] + 50
        y_point_1 = self.pos[1] + 49
        x_point_2 = self.pos[0] + 75
        y_point_2 = self.pos[1] + 49
        x_point_3 = self.pos[0] + 85
        y_point_3 = self.pos[1] + 105
        x_point_4 = self.pos[0] + 40
        y_point_4 = self.pos[1] + 105
        self.body = canvas.create_polygon(x_point_1, y_point_1, x_point_2, y_point_2, x_point_3, y_point_3, x_point_4,
                                          y_point_4,
                                          fill=fill_color, outline="black")
        # This is the left part of the head of the piece
        x_top_left = self.pos[0] + 45
        y_top_left = self.pos[1] + 25
        x_bot_right = self.pos[0] + 65
        y_bot_right = self.pos[1] + 45
        self.left_head = canvas.create_oval(x_top_left, y_top_left, x_bot_right, y_bot_right, fill=fill_color)
        # This is the right part of the head of the piece
        x_top_left = self.pos[0] + 60
        y_top_left = self.pos[1] + 25
        x_bot_right = self.pos[0] + 80
        y_bot_right = self.pos[1] + 45
        self.right_head = canvas.create_oval(x_top_left, y_top_left, x_bot_right, y_bot_right, fill=fill_color)
        # This is the round head of the piece
        x_top_left = self.pos[0] + 55
        y_top_left = self.pos[1] + 18
        x_bot_right = self.pos[0] + 70
        y_bot_right = self.pos[1] + 45
        self.round_head = canvas.create_oval(x_top_left, y_top_left, x_bot_right, y_bot_right, fill=fill_color)
        # This is the tiny round top of the head of the piece
        x_top_left = self.pos[0] + 57
        y_top_left = self.pos[1] + 15
        x_bot_right = self.pos[0] + 68
        y_bot_right = self.pos[1] + 25
        self.tiny_head = canvas.create_oval(x_top_left, y_top_left, x_bot_right, y_bot_right, fill=fill_color)
        # This draws the collar below the round head
        x_top_left = self.pos[0] + 40
        y_top_left = self.pos[1] + 39
        x_bot_right = self.pos[0] + 85
        y_bot_right = self.pos[1] + 49
        self.collar = canvas.create_rectangle(x_top_left, y_top_left, x_bot_right, y_bot_right, fill=fill_color)
        # This draws the base
        x_top_left = self.pos[0] + 20
        y_top_left = self.pos[1] + 105
        x_bot_right = self.pos[0] + 105
        y_bot_right = self.pos[1] + 120
        self.base = canvas.create_rectangle(x_top_left, y_top_left, x_bot_right, y_bot_right, fill=fill_color)
        # This draws the vertical of the cross
        x_top_left = self.pos[0] + 60
        y_top_left = self.pos[1] + 3
        x_bot_right = self.pos[0] + 65
        y_bot_right = self.pos[1] + 17
        self.vertical_cross = canvas.create_rectangle(x_top_left, y_top_left, x_bot_right, y_bot_right, fill=fill_color)
        # This draws the horizontal of the cross
        x_top_left = self.pos[0] + 52
        y_top_left = self.pos[1] + 7
        x_bot_right = self.pos[0] + 73
        y_bot_right = self.pos[1] + 11
        self.horizontal_cross = canvas.create_rectangle(x_top_left, y_top_left, x_bot_right, y_bot_right,
                                                        fill=fill_color)
        # Add everything to the canvas_list so it can be tracked more easily and removed during game loop drawing
        self.shapes = []  # Clear the list of previous shapes
        self.shapes.append(self.horizontal_cross)
        self.shapes.append(self.vertical_cross)
        self.shapes.append(self.base)
        self.shapes.append(self.collar)
        self.shapes.append(self.tiny_head)
        self.shapes.append(self.round_head)
        self.shapes.append(self.right_head)
        self.shapes.append(self.left_head)
        self.shapes.append(self.body)
        canvas_list.append(self.shapes)


class GameBoard:
    def __init__(self, color):
        self.color = color

    def draw(self):
        is_black_square = 1
        for row in range(0, 1000, 125):
            for column in range(0, 1000, 125):
                x_top_left = column
                y_top_left = row
                x_bot_right = column + 125
                y_bot_right = row + 125
                if (is_black_square % 2) == 0:
                    canvas.create_rectangle(x_top_left, y_top_left, x_bot_right, y_bot_right, fill=self.color)
                else:
                    pass
                is_black_square = is_black_square + 1
            is_black_square = is_black_square + 1


class Box:
    def __init__(self, pos, selected_piece, is_active_selection):
        self.pos = pos
        self.selected_piece = selected_piece
        self.is_active_selection = is_active_selection

        # Create self.id for use later when drawing boxes - not sure if this is needed
        self.id = 0
        self.id2 = 0
        # Listen for the 'directional' keys to be pressed
        canvas.bind_all('<KeyPress-Up>', self.move_selection_box)
        canvas.bind_all('<KeyPress-Down>', self.move_selection_box)
        canvas.bind_all('<KeyPress-Left>', self.move_selection_box)
        canvas.bind_all('<KeyPress-Right>', self.move_selection_box)
        canvas.bind_all('<KeyPress-Return>', self.select_game_piece)

    def draw(self):
        box_color = 'red'
        x_top_left_select = self.pos[0]
        y_top_left_select = self.pos[1]
        x_bot_right_select = self.pos[0] + 125
        y_bot_right_select = self.pos[1] + 125
        self.id = canvas.create_rectangle(x_top_left_select, y_top_left_select,
                                          x_bot_right_select, y_bot_right_select, width=3, outline=box_color)
        canvas_list.append(self.id)
        if self.is_active_selection is True:
            box_color = 'yellow'
            x_top_left_selected = self.pos[0] - 2
            y_top_left_selected = self.pos[1] - 2
            x_bot_right_selected = self.pos[0] + 127
            y_bot_right_selected = self.pos[1] + 127
            self.id2 = canvas.create_rectangle(x_top_left_selected, y_top_left_selected,
                                               x_bot_right_selected, y_bot_right_selected, width=3, outline=box_color)
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
        for s in range(len(game_play_info)):
            if square_ask == game_play_info[s].pos:
                # return the obj of the piece on square_ask
                print("Found piece on the square {}.  It's {}.".format(square_ask, game_play_info[s].name))
                return game_play_info[s]
        # no piece on square returns False
        print("There's no piece on square {}.".format(square_ask))
        return False

    def is_square_empty(self, square_ask):
        for s in range(len(game_play_info)):
            if square_ask == game_play_info[s].pos:
                # found a piece on the square, it's not empty, returning False
                print("Found piece on the square {}.  It's {}.".format(square_ask, game_play_info[s].name))
                return False
        # Didn't find any pieces on the square, it's empty, returning True
        print("There's no piece on square {}.".format(square_ask))
        return True

    def move_piece(self):
        for p in range(len(self.selected_piece.shapes)):  # Loop through the shapes drawn for selected piece
            canvas.delete(self.selected_piece.shapes[p])  # Delete each shape from the canvas for the selected piece
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


# Create a game_board object for playing on of Class GameBoard
game_board = GameBoard(board_color)

# Create list for main game play info
game_play_info = [
    # All game pieces are created with their initial position (pos) set at normal game starting position
    # Format for args: name, ref_num, color, pos, alive

    # Create White Pawns as objects of Class Pawn
    Pawn("White Pawn One", 1, white_color, position_a2, [], True, False),
    Pawn("White Pawn Two", 2, white_color, position_b2, [], True, False),
    Pawn("White Pawn Three", 3, white_color, position_c2, [], True, False),
    Pawn("White Pawn Four", 4, white_color, position_d2, [], True, False),
    Pawn("White Pawn Five", 5, white_color, position_e2, [], True, False),
    Pawn("White Pawn Six", 6, white_color, position_f2, [], True, False),
    Pawn("White Pawn Seven", 7, white_color, position_g2, [], True, False),
    Pawn("White Pawn Eight", 8, white_color, position_h2, [], True, False),

    # Create Black Pawns as objects of Class Pawn
    Pawn("Black Pawn One", 9, black_color, position_a7, [], True, False),
    Pawn("Black Pawn Two", 10, black_color, position_b7, [], True, False),
    Pawn("Black Pawn Three", 11, black_color, position_c7, [], True, False),
    Pawn("Black Pawn Four", 12, black_color, position_d7, [], True, False),
    Pawn("Black Pawn Five", 13, black_color, position_e7, [], True, False),
    Pawn("Black Pawn Six", 14, black_color, position_f7, [], True, False),
    Pawn("Black Pawn Seven", 15, black_color, position_g7, [], True, False),
    Pawn("Black Pawn Eight", 16, black_color, position_h7, [], True, False),

    # Create Bishops as objects of Class Bishop
    Bishop("White Bishop One", 17, white_color, position_c1, [], True, False),
    Bishop("White Bishop Two", 18, white_color, position_f1, [], True, False),
    Bishop("Black Bishop One", 19, black_color, position_c8, [], True, False),
    Bishop("Black Bishop Two", 20, black_color, position_f8, [], True, False),

    # Create Rooks as objects of Class Rook
    Rook("White Rook One", 21, white_color, position_a1, [], True, False),
    Rook("White Rook Two", 22, white_color, position_h1, [], True, False),
    Rook("Black Rook One", 23, black_color, position_a8, [], True, False),
    Rook("Black Rook Two", 24, black_color, position_h8, [], True, False),

    # Create Knights as objects of Class Knight
    Knight("White Knight One", 25, white_color, position_b1, [], True, False),
    Knight("White Knight Two", 26, white_color, position_g1, [], True, False),
    Knight("Black Knight One", 27, black_color, position_b8, [], True, False),
    Knight("Black Knight Two", 28, black_color, position_g8, [], True, False),

    # Create Queens as objects of Class Queen
    Queen("White Queen", 29, white_color, position_d1, [], True, False),
    Queen("Black Queen", 30, black_color, position_d8, [], True, False),

    # Create Kings as objects of Class King
    King("White King", 31, white_color, position_e1, [], True, False),
    King("Black King", 32, black_color, position_e8, [], True, False)]

# Draw the game board
game_board.draw()

# Create box for selecting a playing piece of Class Box - initial args are ambiguous and don't really matter
select = Box(position_e4, game_play_info[0], False)

# Main program loop
while 1:
    # Clear the canvas of all objects drawn on the board then clear the list for next cycle
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
