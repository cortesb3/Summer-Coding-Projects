import tkinter as tk
import numpy as np

# keys to move
UP = "'w"
DOWN  = "'s"
RIGHT = "'d"
LEFT = "'a"

# frame constants
EDGE_LENGTH = 400
CELL_COUNT = 4
CELL_PAD = 10 

FONT = ("Verdana", 40, "bold")

GAME_COLOR = "#a6bdbb"

EMPTY_COLOR = "#8eaba8"

TILE_COLORS = {2: "#daeddf", 4: "#9ae3ae", 8: "#6ce68d", 16: "#42ed71",
                   32: "#17e650", 64: "#17c246", 128: "#149938",
                   256: "#107d2e", 512: "#0e6325", 1024: "#0b4a1c",
                   2048: "#031f0a", 4096: "#000000", 8192: "#000000",}

LABEL_COLORS = {2: "#011c08", 4: "#011c08", 8: "#011c08", 16: "#011c08",
                   32: "#011c08", 64: "#f2f2f0", 128: "#f2f2f0",
                   256: "#f2f2f0", 512: "#f2f2f0", 1024: "#f2f2f0",
                   2048: "#f2f2f0", 4096: "#f2f2f0", 8192: "#f2f2f0",}


# game constants
POSSIBLE_MOVES = 4
NUMBER_OF_SQUARES = CELL_COUNT * CELL_COUNT
NEW_TILE_DISTRIBUTION = np.array([2, 2, 2, 2, 2, 2, 2, 2 ,2, 4])


class Game(tk.Frame):
    def __init__(self):
        self.grid()
        self.title("2048")
        self.bind("<Key>", self.key_press)
        
        # self.commands
        
    def build_grid(self):
        pass
    