import copy
import time
import math

from collections import defaultdict

def parse_input(t_cfg):
    line_arr = []
    with open("inex.txt", "r") as in_f:
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
                "X": (int(line_tok[1].split("=")[1].replace(",", "")) + 0), # 10000000000000, 10000000
                "Y": (int(line_tok[2].split("=")[1]) + 0)
            }
            if t_cfg_obj:
                t_cfg.append(t_cfg_obj)
                t_cfg_obj = {}

def get_divs(num):
    divs = defaultdict(int)
    i = 2
    while(i < num/2 + 1):
        if(num%i == 0):
            divs[i] += 1
            num /= i
        else:
            i += 1
    divs[int(num)] += 1
    return divs

def small_comm_mul(a, b):
    ret_val = a*b
    a_divs = get_divs(a)
    b_divs = get_divs(b)
    for a_key in a_divs.keys():
       if(a_key in b_divs.keys()):
        ret_val /= int(a_key**abs(a_divs[a_key] - abs(a_divs[a_key]-b_divs[a_key])))

    return ret_val

def get_inc_pairs(a, b, max):
    inc_pairs = []
    #a_val = 0
    #a_count = 0

    #b_val = 0 
    #b_count = 0

    # Overshooting A
    #a_count = math.floor(max/a) + 1
    #a_val = a * a_count

    # Exact A mult
    """
    if(a_val == max):
        inc_pairs.append([a_count, 0])
        a_val -= a
        a_count -= 1
    """

    # A-B combo
    ab_scm = int(small_comm_mul(a, b))

    start_ts = time.time()
    scm_rem_min_val = 0
    f_found_flag = False
    while not f_found_flag:
        if(((max-scm_rem_min_val)%a == 0 and scm_rem_min_val == 0) or
        ((max-scm_rem_min_val)%a == 0 and (max-scm_rem_min_val)%b == 0)):
            f_found_flag = True
            print(scm_rem_min_val)
        else:
            scm_rem_min_val += 1

    i = 0
    while scm_rem_min_val + i*ab_scm < max:
        a_rem = max - (scm_rem_min_val + i*ab_scm)
        #print((max-a_rem)%b)
        if -1 < (max-a_rem)/b and (max-a_rem)%b == 0:
            inc_pairs.append([a_rem/a, (max-a_rem)/b])
        i+=1

    """
    core_running_flag = True
    first_found = False
    while(core_running_flag):
        #Find first
        if((max - a_val) % b == 0):
            inc_pairs.append([a_count, int((max - a_val)/b)])
            first_found = True
        if not first_found:
            a_val -= a
            a_count -= 1
        else:
            a_val -= ab_scm
            a_count -= ab_scm/a
        if a_val < 0:
            core_running_flag = False
    """

    #print(f"CORE: {time.time() - start_ts}")
    print(f"{inc_pairs}")

    # Exact B mult
    """
    if(max%b == 0):
        inc_pairs.append([0, int(max/b)])
    """
    return inc_pairs

def get_XY_overlaps(X_pairs, Y_pairs):
    ret_arr = []
    start_ts = time.time()
    for X_pair in X_pairs:
        if X_pair in Y_pairs:
            ret_arr.append(X_pair)
    #print(f"PAIRS: {time.time() - start_ts}")
    return ret_arr

def get_token_cost(t_cfg):
    token_cost = 0
    for i, obj in enumerate(t_cfg):
        start_ts = time.time()
        #print(f"START: {i}/{len(t_cfg)}")
        X_pairs = get_inc_pairs(obj["A"]["X"], obj["B"]["X"], obj["goal"]["X"])
        Y_pairs = get_inc_pairs(obj["A"]["Y"], obj["B"]["Y"], obj["goal"]["Y"])
        print("")
        XY_overlaps = get_XY_overlaps(X_pairs, Y_pairs)

        min_token_cost = 0
        for XY_overlap in XY_overlaps:
            overlap_cost = XY_overlap[0] * 3 + XY_overlap[1]
            if min_token_cost == 0:
                min_token_cost = overlap_cost
            elif overlap_cost < min_token_cost:
                min_token_cost = overlap_cost
        token_cost += min_token_cost
        #print(f"{i}/{len(t_cfg)} - {time.time() - start_ts}")
    return token_cost

t_cfg = []
start_ts = time.time()
parse_input(t_cfg)
print(get_token_cost(t_cfg))
print(f"RUNTIME: {time.time() - start_ts}")