# This is an educational project "Chessboard" by Todd Aitkins and is "Open Source" - 2020

from tkinter import *  # TODO consider changing import to only specified/required methods (avoid namespace conflicts)
import time

# -Global variable definitions-
white_color = 'white'
black_color = 'black'
board_color = 'gray'
piece_fill_color_black = '#303030'
piece_fill_color_black_selected = 'green'
piece_fill_color_white = 'white'
piece_fill_color_white_selected = 'green'
is_selected_pos = False
board_position = {}  # Create a dict to contain a map for all the board positions
canvas_list = []


def build_board_positions():
    """
    This is a static method that will build a dict containing 64 entries for the board positions.
    The key() is a string name of the Position in algebraic form (a1, a2,...b1...etc.) and value
    is the upper left corner of the chessboard square in pixels [x, y] based on Tkinter canvas
    reference points.
    """
    global board_position
    board_build_x_dict = {0: "a", 125: "b", 250: "c", 375: "d", 500: "e", 625: "f", 750: "g", 875: "h"}
    board_build_y_dict = {0: 8, 125: 7, 250: 6, 375: 5, 500: 4, 625: 3, 750: 2, 875: 1}
    for x in range(0, 876, 125):
        for y in range(875, -1, -125):
            temp_pos_name = "Position {}{}".format(board_build_x_dict[x], board_build_y_dict[y])
            temp_pos_list = [x, y]
            board_position[temp_pos_name] = temp_pos_list


def set_color_piece(piece_color, is_selected):  # set colors for piece
    """This function will check the objects attributes and determine the correct fill_color to return"""
    if (piece_color == black_color) and (is_selected is True):
        return piece_fill_color_black_selected
    elif (piece_color == black_color) and (is_selected is False):
        return piece_fill_color_black
    elif (piece_color == white_color) and (is_selected is True):
        return piece_fill_color_white_selected
    else:
        return piece_fill_color_white


class Game:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("Worlds Greatest Chess Game!")
        self.tk.resizable(0, 0)
        self.tk.wm_attributes("-topmost", 1)

        # define the drawing space
        self.canvas = Canvas(self.tk, width=1000, height=1000)
        self.canvas.pack()
        build_board_positions()

    def __str__(self):
        return 'Chess Game obj'

    def mainloop(self):  # Main program loop
        game_board.draw()  # Draw the game board

        for i in range(0, len(game_play_info)):  # Loop game_play_info and call each .draw for pieces
            game_play_info[i].draw()

        select.draw()  # Draw selection box

        while 1:  # Keep game running until window closes
            self.tk.update_idletasks()
            self.tk.update()
            time.sleep(.1)


class ChessPiece:
    def __init__(self, game, name, ref_num, color, pos, shapes, alive, is_selected):
        self.game = game
        self.name = name
        self.ref_num = ref_num
        self.color = color
        self.pos = pos
        self.shapes = shapes
        self.alive = alive
        self.is_selected = is_selected


class Pawn(ChessPiece):
    def __init__(self, *args, **kwargs):
        super(Pawn, self).__init__(*args, **kwargs)
        self.base = self.collar = self.head = self.body = None

    def __str__(self):
        return self.name

    # Draw the pawn
    def draw(self):
        if not self.alive:
            return
        fill_color = set_color_piece(self.color, self.is_selected)  # set colors for piece
        # This draws the base
        x_top_left = self.pos[0] + 20
        y_top_left = self.pos[1] + 105
        x_bot_right = self.pos[0] + 105
        y_bot_right = self.pos[1] + 120
        if self.base != 0:
            self.game.canvas.delete(self.base)
        self.base = self.game.canvas.create_rectangle(x_top_left, y_top_left, x_bot_right, y_bot_right, fill=fill_color)
        # This draws the collar below the round head
        x_top_left = self.pos[0] + 40
        y_top_left = self.pos[1] + 45
        x_bot_right = self.pos[0] + 85
        y_bot_right = self.pos[1] + 55
        if self.collar != 0:
            self.game.canvas.delete(self.collar)
        self.collar = self.game.canvas.create_rectangle(x_top_left, y_top_left, x_bot_right, y_bot_right,
                                                        fill=fill_color)
        # This is the round head of the piece
        x_top_left = self.pos[0] + 50
        y_top_left = self.pos[1] + 20
        x_bot_right = self.pos[0] + 75
        y_bot_right = self.pos[1] + 45
        if self.head != 0:
            self.game.canvas.delete(self.head)
        self.head = self.game.canvas.create_oval(x_top_left, y_top_left, x_bot_right, y_bot_right, fill=fill_color)
        # This draws the polygon to represent the body
        x_point_1 = self.pos[0] + 50
        y_point_1 = self.pos[1] + 55
        x_point_2 = self.pos[0] + 75
        y_point_2 = self.pos[1] + 55
        x_point_3 = self.pos[0] + 85
        y_point_3 = self.pos[1] + 105
        x_point_4 = self.pos[0] + 40
        y_point_4 = self.pos[1] + 105
        if self.body != 0:
            self.game.canvas.delete(self.body)
        self.body = self.game.canvas.create_polygon(x_point_1, y_point_1, x_point_2, y_point_2, x_point_3, y_point_3,
                                                    x_point_4, y_point_4, fill=fill_color, outline="black")
        # Add everything to the canvas_list so it can be tracked more easily and removed during game loop drawing
        self.shapes = []  # Clear the list of previous shapes
        self.shapes.append(self.base)
        self.shapes.append(self.collar)
        self.shapes.append(self.head)
        self.shapes.append(self.body)
        canvas_list.append(self.shapes)

    def is_move_valid(self, from_pos, to_pos):  # TODO finish this function and call it somewhere
        pass
        # is it first move - then you can move further
        # is black - can move down
        # is white - can move up


class Bishop(ChessPiece):
    def __init__(self, *args, **kwargs):
        super(Bishop, self).__init__(*args, **kwargs)
        self.base = self.collar = self.tiny_head = self.head = self.body = None

    def draw(self):
        if not self.alive:
            return
        fill_color = set_color_piece(self.color, self.is_selected)  # set colors for piece
        # This draws the polygon to represent the body
        x_point_1 = self.pos[0] + 50
        y_point_1 = self.pos[1] + 49
        x_point_2 = self.pos[0] + 75
        y_point_2 = self.pos[1] + 49
        x_point_3 = self.pos[0] + 85
        y_point_3 = self.pos[1] + 105
        x_point_4 = self.pos[0] + 40
        y_point_4 = self.pos[1] + 105
        if self.body != 0:
            self.game.canvas.delete(self.body)
        self.body = self.game.canvas.create_polygon(x_point_1, y_point_1, x_point_2, y_point_2, x_point_3, y_point_3,
                                                    x_point_4, y_point_4, fill=fill_color, outline="black")
        # This is the round head of the piece
        x_top_left = self.pos[0] + 50
        y_top_left = self.pos[1] + 12
        x_bot_right = self.pos[0] + 75
        y_bot_right = self.pos[1] + 45
        if self.head != 0:
            self.game.canvas.delete(self.head)
        self.head = self.game.canvas.create_oval(x_top_left, y_top_left, x_bot_right, y_bot_right, fill=fill_color)
        # This is the tiny round top of the head of the piece
        x_top_left = self.pos[0] + 57
        y_top_left = self.pos[1] + 5
        x_bot_right = self.pos[0] + 68
        y_bot_right = self.pos[1] + 15
        if self.tiny_head != 0:
            self.game.canvas.delete(self.tiny_head)
        self.tiny_head = self.game.canvas.create_oval(x_top_left, y_top_left, x_bot_right, y_bot_right, fill=fill_color)
        # This draws the collar below the round head
        x_top_left = self.pos[0] + 40
        y_top_left = self.pos[1] + 39
        x_bot_right = self.pos[0] + 85
        y_bot_right = self.pos[1] + 49
        if self.collar != 0:
            self.game.canvas.delete(self.collar)
        self.collar = self.game.canvas.create_rectangle(x_top_left, y_top_left, x_bot_right, y_bot_right,
                                                        fill=fill_color)
        # This draws the base
        x_top_left = self.pos[0] + 20
        y_top_left = self.pos[1] + 105
        x_bot_right = self.pos[0] + 105
        y_bot_right = self.pos[1] + 120
        if self.base != 0:
            self.game.canvas.delete(self.base)
        self.base = self.game.canvas.create_rectangle(x_top_left, y_top_left, x_bot_right, y_bot_right, fill=fill_color)
        # Add everything to the canvas_list so it can be tracked more easily and removed during game loop drawing
        self.shapes = []  # Clear the list of previous shapes
        self.shapes.append(self.base)
        self.shapes.append(self.collar)
        self.shapes.append(self.tiny_head)
        self.shapes.append(self.head)
        self.shapes.append(self.body)
        canvas_list.append(self.shapes)


class Rook(ChessPiece):
    def __init__(self, *args, **kwargs):
        super(Rook, self).__init__(*args, **kwargs)
        self.base = self.head = self.body = None

    def draw(self):
        if not self.alive:
            return
        fill_color = set_color_piece(self.color, self.is_selected)  # set colors for piece
        # This draws the polygon to represent the body
        x_point_1 = self.pos[0] + 50
        y_point_1 = self.pos[1] + 49
        x_point_2 = self.pos[0] + 75
        y_point_2 = self.pos[1] + 49
        x_point_3 = self.pos[0] + 85
        y_point_3 = self.pos[1] + 105
        x_point_4 = self.pos[0] + 40
        y_point_4 = self.pos[1] + 105
        if self.body != 0:
            self.game.canvas.delete(self.body)
        self.body = self.game.canvas.create_polygon(x_point_1, y_point_1, x_point_2, y_point_2, x_point_3, y_point_3,
                                                    x_point_4, y_point_4, fill=fill_color, outline="black")
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
        if self.head != 0:
            self.game.canvas.delete(self.head)
        self.head = self.game.canvas.create_polygon(x_point_1, y_point_1, x_point_2, y_point_2, x_point_3, y_point_3,
                                                    x_point_4, y_point_4, x_point_5, y_point_5, x_point_6, y_point_6,
                                                    x_point_7, y_point_7, x_point_8, y_point_8, x_point_9, y_point_9,
                                                    x_point_10, y_point_10, x_point_11, y_point_11, x_point_12,
                                                    y_point_12, fill=fill_color, outline="black")
        # This draws the base
        x_top_left = self.pos[0] + 20
        y_top_left = self.pos[1] + 105
        x_bot_right = self.pos[0] + 105
        y_bot_right = self.pos[1] + 120
        if self.base != 0:
            self.game.canvas.delete(self.base)
        self.base = self.game.canvas.create_rectangle(x_top_left, y_top_left, x_bot_right, y_bot_right, fill=fill_color)
        # Add everything to the canvas_list so it can be tracked more easily and removed during game loop drawing
        self.shapes = []  # Clear the list of previous shapes
        self.shapes.append(self.base)
        self.shapes.append(self.head)
        self.shapes.append(self.body)
        canvas_list.append(self.shapes)


class Knight(ChessPiece):
    def __init__(self, *args, **kwargs):
        super(Knight, self).__init__(*args, **kwargs)
        self.base = self.body = None

    def draw(self):
        if not self.alive:
            return
        fill_color = set_color_piece(self.color, self.is_selected)  # set colors for piece
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
        if self.body != 0:
            self.game.canvas.delete(self.body)
        self.body = self.game.canvas.create_polygon(x_point_1, y_point_1, x_point_2, y_point_2, x_point_3, y_point_3,
                                                    x_point_4, y_point_4, x_point_5, y_point_5, x_point_6, y_point_6,
                                                    x_point_7, y_point_7, x_point_8, y_point_8, x_point_9, y_point_9,
                                                    x_point_10, y_point_10, x_point_11, y_point_11, x_point_12,
                                                    y_point_12, x_point_13, y_point_13, x_point_14, y_point_14,
                                                    x_point_15, y_point_15, x_point_16, y_point_16, fill=fill_color,
                                                    outline="black")
        # This draws the base
        x_top_left = self.pos[0] + 20
        y_top_left = self.pos[1] + 105
        x_bot_right = self.pos[0] + 105
        y_bot_right = self.pos[1] + 120
        if self.base != 0:
            self.game.canvas.delete(self.base)
        self.base = self.game.canvas.create_rectangle(x_top_left, y_top_left, x_bot_right, y_bot_right, fill=fill_color)
        # Add everything to the canvas_list so it can be tracked more easily and removed during game loop drawing
        self.shapes = []  # Clear the list of previous shapes
        self.shapes.append(self.base)
        self.shapes.append(self.body)
        canvas_list.append(self.shapes)


class Queen(ChessPiece):
    def __init__(self, *args, **kwargs):
        super(Queen, self).__init__(*args, **kwargs)
        self.base = self.head = self.body = None

    def draw(self):
        if not self.alive:
            return
        fill_color = set_color_piece(self.color, self.is_selected)  # set colors for piece
        # This draws the polygon to represent the body
        x_point_1 = self.pos[0] + 50
        y_point_1 = self.pos[1] + 40
        x_point_2 = self.pos[0] + 75
        y_point_2 = self.pos[1] + 40
        x_point_3 = self.pos[0] + 85
        y_point_3 = self.pos[1] + 105
        x_point_4 = self.pos[0] + 40
        y_point_4 = self.pos[1] + 105
        if self.body != 0:
            self.game.canvas.delete(self.body)
        self.body = self.game.canvas.create_polygon(x_point_1, y_point_1, x_point_2, y_point_2, x_point_3, y_point_3,
                                                    x_point_4, y_point_4, fill=fill_color, outline="black")
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
        if self.head != 0:
            self.game.canvas.delete(self.head)
        self.head = self.game.canvas.create_polygon(x_point_1, y_point_1, x_point_2, y_point_2, x_point_3, y_point_3,
                                                    x_point_4, y_point_4, x_point_5, y_point_5, x_point_6, y_point_6,
                                                    x_point_7, y_point_7, x_point_8, y_point_8, x_point_9, y_point_9,
                                                    x_point_10, y_point_10, x_point_11, y_point_11, x_point_12,
                                                    y_point_12, x_point_13, y_point_13, x_point_14, y_point_14,
                                                    x_point_15, y_point_15, x_point_16, y_point_16, x_point_17,
                                                    y_point_17, x_point_18, y_point_18, x_point_19, y_point_19,
                                                    x_point_20, y_point_20, fill=fill_color, outline="black")
        # This draws the base
        x_top_left = self.pos[0] + 20
        y_top_left = self.pos[1] + 105
        x_bot_right = self.pos[0] + 105
        y_bot_right = self.pos[1] + 120
        if self.base != 0:
            self.game.canvas.delete(self.base)
        self.base = self.game.canvas.create_rectangle(x_top_left, y_top_left, x_bot_right, y_bot_right,
                                                      fill=fill_color)
        # Add everything to the canvas_list so it can be tracked more easily and removed during game loop drawing
        self.shapes = []  # Clear the list of previous shapes
        self.shapes.append(self.base)
        self.shapes.append(self.head)
        self.shapes.append(self.body)
        canvas_list.append(self.shapes)


class King(ChessPiece):
    def __init__(self, *args, **kwargs):
        super(King, self).__init__(*args, **kwargs)
        self.horizontal_cross = self.vertical_cross = self.base = self.collar = self.tiny_head = self.round_head = \
            self.right_head = self.left_head = self.body = None

    def draw(self):
        if not self.alive:
            return
        fill_color = set_color_piece(self.color, self.is_selected)  # set colors for piece
        # This draws the polygon to represent the body
        x_point_1 = self.pos[0] + 50
        y_point_1 = self.pos[1] + 49
        x_point_2 = self.pos[0] + 75
        y_point_2 = self.pos[1] + 49
        x_point_3 = self.pos[0] + 85
        y_point_3 = self.pos[1] + 105
        x_point_4 = self.pos[0] + 40
        y_point_4 = self.pos[1] + 105
        if self.body != 0:
            self.game.canvas.delete(self.body)
        self.body = self.game.canvas.create_polygon(x_point_1, y_point_1, x_point_2, y_point_2, x_point_3, y_point_3,
                                                    x_point_4, y_point_4, fill=fill_color, outline="black")
        # This is the left part of the head of the piece
        x_top_left = self.pos[0] + 45
        y_top_left = self.pos[1] + 25
        x_bot_right = self.pos[0] + 65
        y_bot_right = self.pos[1] + 45
        if self.left_head != 0:
            self.game.canvas.delete(self.left_head)
        self.left_head = self.game.canvas.create_oval(x_top_left, y_top_left, x_bot_right, y_bot_right, fill=fill_color)
        # This is the right part of the head of the piece
        x_top_left = self.pos[0] + 60
        y_top_left = self.pos[1] + 25
        x_bot_right = self.pos[0] + 80
        y_bot_right = self.pos[1] + 45
        if self.right_head != 0:
            self.game.canvas.delete(self.right_head)
        self.right_head = self.game.canvas.create_oval(x_top_left, y_top_left, x_bot_right, y_bot_right,
                                                       fill=fill_color)
        # This is the round head of the piece
        x_top_left = self.pos[0] + 55
        y_top_left = self.pos[1] + 18
        x_bot_right = self.pos[0] + 70
        y_bot_right = self.pos[1] + 45
        if self.round_head != 0:
            self.game.canvas.delete(self.round_head)
        self.round_head = self.game.canvas.create_oval(x_top_left, y_top_left, x_bot_right, y_bot_right,
                                                       fill=fill_color)
        # This is the tiny round top of the head of the piece
        x_top_left = self.pos[0] + 57
        y_top_left = self.pos[1] + 15
        x_bot_right = self.pos[0] + 68
        y_bot_right = self.pos[1] + 25
        if self.tiny_head != 0:
            self.game.canvas.delete(self.tiny_head)
        self.tiny_head = self.game.canvas.create_oval(x_top_left, y_top_left, x_bot_right, y_bot_right, fill=fill_color)
        # This draws the collar below the round head
        x_top_left = self.pos[0] + 40
        y_top_left = self.pos[1] + 39
        x_bot_right = self.pos[0] + 85
        y_bot_right = self.pos[1] + 49
        if self.collar != 0:
            self.game.canvas.delete(self.collar)
        self.collar = self.game.canvas.create_rectangle(x_top_left, y_top_left, x_bot_right, y_bot_right,
                                                        fill=fill_color)
        # This draws the base
        x_top_left = self.pos[0] + 20
        y_top_left = self.pos[1] + 105
        x_bot_right = self.pos[0] + 105
        y_bot_right = self.pos[1] + 120
        if self.base != 0:
            self.game.canvas.delete(self.base)
        self.base = self.game.canvas.create_rectangle(x_top_left, y_top_left, x_bot_right, y_bot_right, fill=fill_color)
        # This draws the vertical of the cross
        x_top_left = self.pos[0] + 60
        y_top_left = self.pos[1] + 3
        x_bot_right = self.pos[0] + 65
        y_bot_right = self.pos[1] + 17
        if self.vertical_cross != 0:
            self.game.canvas.delete(self.vertical_cross)
        self.vertical_cross = self.game.canvas.create_rectangle(x_top_left, y_top_left, x_bot_right, y_bot_right,
                                                                fill=fill_color)
        # This draws the horizontal of the cross
        x_top_left = self.pos[0] + 52
        y_top_left = self.pos[1] + 7
        x_bot_right = self.pos[0] + 73
        y_bot_right = self.pos[1] + 11
        if self.horizontal_cross != 0:
            self.game.canvas.delete(self.horizontal_cross)
        self.horizontal_cross = self.game.canvas.create_rectangle(x_top_left, y_top_left, x_bot_right, y_bot_right,
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
    def __init__(self, game, color):
        self.game = game
        self.color = color

    # Expecting to call the draw method only once at the beginning of mainloop.
    # Canvas is not cleaned up before drawing board.
    def draw(self):
        is_black_square = 1
        for row in range(0, 1000, 125):
            for column in range(0, 1000, 125):
                x_top_left = column
                y_top_left = row
                x_bot_right = column + 125
                y_bot_right = row + 125
                if (is_black_square % 2) == 0:
                    self.game.canvas.create_rectangle(x_top_left, y_top_left, x_bot_right, y_bot_right, fill=self.color)
                else:
                    pass
                is_black_square = is_black_square + 1
            is_black_square = is_black_square + 1


class Box:
    def __init__(self, game, pos, selected_piece, is_active_selection):
        self.game = game
        self.pos = pos
        self.selected_piece = selected_piece
        self.is_active_selection = is_active_selection

        # Create self.id for use later when drawing boxes - not sure if this is needed
        self.id = 0
        self.id2 = 0
        # Listen for the 'directional' keys to be pressed
        self.game.canvas.bind_all('<KeyPress-Up>', self.move_selection_box)
        self.game.canvas.bind_all('<KeyPress-Down>', self.move_selection_box)
        self.game.canvas.bind_all('<KeyPress-Left>', self.move_selection_box)
        self.game.canvas.bind_all('<KeyPress-Right>', self.move_selection_box)
        self.game.canvas.bind_all('<KeyPress-Return>', self.enter_press)

    def draw(self):
        box_color = 'red'
        x_top_left_select = self.pos[0]
        y_top_left_select = self.pos[1]
        x_bot_right_select = self.pos[0] + 125
        y_bot_right_select = self.pos[1] + 125
        if self.id != 0:
            self.game.canvas.delete(self.id)
            self.game.canvas.delete(self.id2)
        self.id = self.game.canvas.create_rectangle(x_top_left_select, y_top_left_select, x_bot_right_select,
                                                    y_bot_right_select, width=3, outline=box_color)
        canvas_list.append(self.id)
        if self.is_active_selection is True:
            box_color = 'yellow'
            x_top_left_selected = self.pos[0] - 2
            y_top_left_selected = self.pos[1] - 2
            x_bot_right_selected = self.pos[0] + 127
            y_bot_right_selected = self.pos[1] + 127
            self.id2 = self.game.canvas.create_rectangle(x_top_left_selected, y_top_left_selected,
                                                         x_bot_right_selected, y_bot_right_selected, width=3,
                                                         outline=box_color)
            canvas_list.append(self.id2)

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

    def exec_box_move(self, new_x, new_y):
        self.pos[0] = self.pos[0] + new_x  # Change the  x position
        self.pos[1] = self.pos[1] + new_y  # Change the  y position
        self.draw()  # Draw new box

    def enter_press(self, event):
        if event.keysym == 'Return':
            if not self.is_active_selection and self.is_square_empty():  # No active selection and square empty
                print("You can't select an empty square, you have to pick a piece first.")

            elif not self.is_active_selection and not self.is_square_empty():  # No active select. and square not empty
                self.select_piece()
                print("You selected the {} piece.".format(self.return_piece_on_square().name))

            elif self.is_active_selection and self.is_square_empty():  # Active selection and new square empty
                print("There's no piece on square {}.  It's empty, so that's a valid move.".format(self.pos))
                self.move_piece()

            elif self.is_active_selection and not self.is_square_empty():  # Active selection and new square not empty
                print("Found {} piece on the square {}.".format(self.return_piece_on_square().name, self.pos))
                print("You can't move your piece to an occupied square silly.")

            else:
                print("Error:  enter_press function logic not met for all possible cases.")

        else:
            print("Error:  enter_press function called and event didn't match.")

    def return_piece_on_square(self):
        # found_piece = False
        for piece in range(0, len(game_play_info)):
            if self.pos == game_play_info[piece].pos:
                # found_piece = True
                return game_play_info[piece]
        # if not found_piece:
        #     print("Error:  There's no piece on square {}.  It's empty.".format(self.pos))
        #     return None

    def is_square_empty(self):
        if self.return_piece_on_square():  # if True (i.e. function returns an obj therefore it has a piece)
            return False
        elif not self.return_piece_on_square():
            return True
        else:
            print("Error:  is_square_empty function called and self.return_piece_square() failed logic.")

    def select_piece(self):
        self.is_active_selection = True  # Change state of box
        self.draw()  # Redraw the box
        self.return_piece_on_square().is_selected = True  # change state of piece
        self.return_piece_on_square().draw()  # redraw piece
        self.selected_piece = self.return_piece_on_square()  # Store the selected piece in self.selected_piece

    def move_piece(self):
        self.selected_piece.pos = self.pos.copy()  # Copy self.pos list to self.selected_piece.pos to update position
        self.return_piece_on_square().is_selected = False  # change state of piece
        self.selected_piece.draw()  # redraw piece
        self.selected_piece = None  # remove obj
        self.is_active_selection = False  # Change state of box
        self.draw()  # Redraw the box


# Create a g instance of Game
g = Game()

# Create a game_board object for playing on of Class GameBoard
game_board = GameBoard(g, board_color)

# Create list for main game play info and all Chess pieces inside of the list
game_play_info = [
    # All game pieces are created with their initial position (pos) set at normal game starting position
    # Format for args: name, ref_num, color, pos, alive

    # Create White Pawns as objects of Class Pawn
    Pawn(g, "White Pawn One", 1, white_color, board_position["Position a2"], [], True, False),
    Pawn(g, "White Pawn Two", 2, white_color, board_position["Position b2"], [], True, False),
    Pawn(g, "White Pawn Three", 3, white_color, board_position["Position c2"], [], True, False),
    Pawn(g, "White Pawn Four", 4, white_color, board_position["Position d2"], [], True, False),
    Pawn(g, "White Pawn Five", 5, white_color, board_position["Position e2"], [], True, False),
    Pawn(g, "White Pawn Six", 6, white_color, board_position["Position f2"], [], True, False),
    Pawn(g, "White Pawn Seven", 7, white_color, board_position["Position g2"], [], True, False),
    Pawn(g, "White Pawn Eight", 8, white_color, board_position["Position h2"], [], True, False),

    # Create Black Pawns as objects of Class Pawn
    Pawn(g, "Black Pawn One", 9, black_color, board_position["Position a7"], [], True, False),
    Pawn(g, "Black Pawn Two", 10, black_color, board_position["Position b7"], [], True, False),
    Pawn(g, "Black Pawn Three", 11, black_color, board_position["Position c7"], [], True, False),
    Pawn(g, "Black Pawn Four", 12, black_color, board_position["Position d7"], [], True, False),
    Pawn(g, "Black Pawn Five", 13, black_color, board_position["Position e7"], [], True, False),
    Pawn(g, "Black Pawn Six", 14, black_color, board_position["Position f7"], [], True, False),
    Pawn(g, "Black Pawn Seven", 15, black_color, board_position["Position g7"], [], True, False),
    Pawn(g, "Black Pawn Eight", 16, black_color, board_position["Position h7"], [], True, False),

    # Create Bishops as objects of Class Bishop
    Bishop(g, "White Bishop One", 17, white_color, board_position["Position c1"], [], True, False),
    Bishop(g, "White Bishop Two", 18, white_color, board_position["Position f1"], [], True, False),
    Bishop(g, "Black Bishop One", 19, black_color, board_position["Position c8"], [], True, False),
    Bishop(g, "Black Bishop Two", 20, black_color, board_position["Position f8"], [], True, False),

    # Create Rooks as objects of Class Rook
    Rook(g, "White Rook One", 21, white_color, board_position["Position a1"], [], True, False),
    Rook(g, "White Rook Two", 22, white_color, board_position["Position h1"], [], True, False),
    Rook(g, "Black Rook One", 23, black_color, board_position["Position a8"], [], True, False),
    Rook(g, "Black Rook Two", 24, black_color, board_position["Position h8"], [], True, False),

    # Create Knights as objects of Class Knight
    Knight(g, "White Knight One", 25, white_color, board_position["Position b1"], [], True, False),
    Knight(g, "White Knight Two", 26, white_color, board_position["Position g1"], [], True, False),
    Knight(g, "Black Knight One", 27, black_color, board_position["Position b8"], [], True, False),
    Knight(g, "Black Knight Two", 28, black_color, board_position["Position g8"], [], True, False),

    # Create Queens as objects of Class Queen
    Queen(g, "White Queen", 29, white_color, board_position["Position d1"], [], True, False),
    Queen(g, "Black Queen", 30, black_color, board_position["Position d8"], [], True, False),

    # Create Kings as objects of Class King
    King(g, "White King", 31, white_color, board_position["Position e1"], [], True, False),
    King(g, "Black King", 32, black_color, board_position["Position e8"], [], True, False)]

# Create box for selecting a playing piece of Class Box - initial args are ambiguous and don't really matter
select = Box(g, board_position["Position e4"], None, False)

g.mainloop()
