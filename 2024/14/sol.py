import copy
import time
import re

class Robot:
    x: int
    y: int
    v_x: int
    v_y: int

    def __init__(self, x, y, v_x, v_y):
        self.x = int(x)
        self.y = int(y)
        self.v_x = int(v_x)
        self.v_y = int(v_y)

    def move(self, TILE_CFG):
        pot_x = self.x + self.v_x
        pot_y = self.y + self.v_y

        if -1 < pot_x and pot_x < TILE_CFG["W"]:
            self.x = pot_x
        else:
            if(pot_x < 0):
                self.x = pot_x + TILE_CFG["W"]
            else:
                self.x = pot_x - TILE_CFG["W"]

        if -1 < pot_y and pot_y < TILE_CFG["H"]:
            self.y = pot_y
        else:
            if(pot_y < 0):
                self.y = pot_y + TILE_CFG["H"]
            else:
                self.y = pot_y - TILE_CFG["H"]

    def get_quad(self, TILE_CFG):
        if(self.x < (TILE_CFG["W"] - 1)/2 and self.y < (TILE_CFG["H"] - 1)/2):
            return 0
        if((TILE_CFG["W"] - 1)/2 < self.x and self.y < (TILE_CFG["H"] - 1)/2):
            return 1
        if(self.x < (TILE_CFG["W"] - 1)/2 and (TILE_CFG["H"] - 1)/2 < self.y):
            return 2
        if((TILE_CFG["W"] - 1)/2 < self.x and (TILE_CFG["H"] - 1)/2 < self.y):
            return 3
        return 4

    def to_str(self):
        return f"x: {self.x}, y: {self.y}, v_x: {self.v_x}, v_y: {self.v_y}"

def parse_input(rob_arr):
    with open("in.txt", "r") as in_f:
        for line in in_f:
            ws_tok = re.split(r"\s|=|,", line.strip())
            rob_arr.append(Robot(ws_tok[1], ws_tok[2], ws_tok[4], ws_tok[5]))

TILE_CFG = {"W": 101, "H": 103}
rob_arr = []
parse_input(rob_arr)

SECS = 100
for rob in rob_arr:
    for _ in range(SECS):
        rob.move(TILE_CFG)

r_quad_count = [0, 0, 0, 0, 0] # TL, TR, BL, BR, MID
for rob in rob_arr:
    quad_idx = rob.get_quad(TILE_CFG)
    r_quad_count[quad_idx] += 1

print(r_quad_count[0]*r_quad_count[1]*r_quad_count[2]*r_quad_count[3])