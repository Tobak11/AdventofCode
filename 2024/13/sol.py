import copy
import time

def parse_input(t_cfg):
    line_arr = []
    with open("in.txt", "r") as in_f:
        for line in in_f:
            line_strip = line.strip()
            if(line_strip):
                line_arr.append(line_strip)

    t_cfg_obj = {}
    for line in line_arr:
        if "A" in line:
            line_tok = line.strip().split(" ")
            t_cfg_obj["A"] = {
                "X": int(line_tok[2].split("+")[1].replace(",", "")),
                "Y": int(line_tok[3].split("+")[1])
            }
        elif "B" in line:
            line_tok = line.strip().split(" ")
            t_cfg_obj["B"] = {
                "X": int(line_tok[2].split("+")[1].replace(",", "")), 
                "Y": int(line_tok[3].split("+")[1])
            }
        elif "=" in line:
            line_tok = line.strip().split(" ")
            t_cfg_obj["goal"] = {
                "X": int(line_tok[1].split("=")[1].replace(",", "")), 
                "Y": int(line_tok[2].split("=")[1])
            }
            if t_cfg_obj:
                t_cfg.append(t_cfg_obj)
                t_cfg_obj = {}

def get_inc_pairs(a, b, max):
    inc_pairs = []
    a_val = 0
    a_count = 0

    b_val = 0 
    b_count = 0
    # Overshooting A
    while(a_val < max):
        a_val += a
        a_count += 1

    # Exact A mult
    if(a_val == max):
        inc_pairs.append([a_count, 0])
        a_val -= a
        a_count -= 1
    
    # A-B combo
    while(0 != a_val):
        if((max - a_val) % b == 0):
            inc_pairs.append([a_count, int((max - a_val)/b)])
        a_val -= a
        a_count -= 1

    # Exact B mult
    if(max%b == 0):
        inc_pairs.append([0, int(max/b)])
    return inc_pairs

def get_XY_overlaps(X_pairs, Y_pairs):
    ret_arr = []
    for X_pair in X_pairs:
        if X_pair in Y_pairs:
            ret_arr.append(X_pair)
    return ret_arr

def get_token_cost(t_cfg):
    token_cost = 0
    for obj in t_cfg:
        X_pairs = get_inc_pairs(obj["A"]["X"], obj["B"]["X"], obj["goal"]["X"])
        Y_pairs = get_inc_pairs(obj["A"]["Y"], obj["B"]["Y"], obj["goal"]["Y"])
        XY_overlaps = get_XY_overlaps(X_pairs, Y_pairs)

        min_token_cost = 0
        for XY_overlap in XY_overlaps:
            overlap_cost = XY_overlap[0] * 3 + XY_overlap[1]
            if min_token_cost == 0:
                min_token_cost = overlap_cost
            elif overlap_cost < min_token_cost:
                min_token_cost = overlap_cost
        token_cost += min_token_cost
    return token_cost

t_cfg = []
parse_input(t_cfg)
print(get_token_cost(t_cfg))