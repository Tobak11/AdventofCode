import copy
import time

def norm_str_to_num(str_num):    
    only_zero_flag = True
    for c in str_num:
        if(c != '0'):
            only_zero_flag = False
    if only_zero_flag:
        return 0

    cleaned_str_num = ""
    lead_zero_flag = True
    for c in str_num:
        if(c != '0'):
            lead_zero_flag = False
        if not lead_zero_flag:
            cleaned_str_num += c
    return int(cleaned_str_num)

def app_rules(stone):
    if(stone == 0):
        return [1]
    if(len(str(stone)) % 2 == 0):
        str_stone = str(stone)
        return [int(str_stone[0:int(len(str_stone)/2)]), norm_str_to_num(str_stone[int(len(str_stone)/2):len(str_stone)])]
    return [stone * 2024]
    
def blink(stones):
    temp_arr = []
    
    for stone in stones:
        temp_arr += app_rules(stone)
    return temp_arr

def blink_v2(idx, stones, digit_mapping, digit_idx_map):
    temp_arr = []
    
    # Get expiring indexes
    reidx_arr = []
    for dim_key in digit_idx_map.keys():
        dim_idx = 0
        while(dim_idx < len(digit_idx_map[dim_key])):
            if(idx == digit_idx_map[dim_key][dim_idx]):
                reidx_arr += digit_mapping[dim_key]
                digit_idx_map[dim_key].pop(dim_idx)
                dim_idx -= 1
            dim_idx += 1
    
    for el in reidx_arr:
        if el == 0:
            digit_idx_map[el].append(idx + 3)
        elif 1 <= el and el <= 4:
            digit_idx_map[el].append(idx + 2)
        else:
            digit_idx_map[el].append(idx + 4)
    
    for stone in stones:
        if(len(str(stone)) == 1):
            if stone == 0:
                digit_idx_map[stone].append(idx + 3)
            elif 1 <= stone and stone <= 4:
                digit_idx_map[stone].append(idx + 2)
            else:
                digit_idx_map[stone].append(idx + 4)
        else:
            temp_arr += app_rules(stone)
        
    return temp_arr

def proc_digidxmap(digit_idx_map, digit_remainder, max_idx):
    sum = 0
    for dim_key in digit_idx_map.keys():
        for idx in digit_idx_map[dim_key]:
            sum += digit_remainder[dim_key][idx - max_idx]
    return sum

digit_remainder = {
    0: ["_", 2, 1],
    1: ["_", 2, 1],
    2: ["_", 2, 1],
    3: ["_", 2, 1],
    4: ["_", 2, 1],
    5: ["_", 4, 2, 1, 1],
    6: ["_", 4, 2, 1, 1],
    7: ["_", 4, 2, 1, 1],
    8: ["_", 4, 2, 1, 1],
    9: ["_", 4, 2, 1, 1],
}

digit_mapping = {
    0: [2, 0, 2, 4],
    1: [2, 0, 2, 4],
    2: [4, 0, 4, 8],
    3: [6, 0, 7, 2],
    4: [8, 0, 9, 6],
    5: [2, 0, 4, 8, 2, 8, 8, 0],
    6: [2, 4, 5, 7, 9, 4, 5, 6],
    7: [2, 8, 6, 7, 6, 0, 3, 2],
    8: [3, 2, 7, 7, 2, 6, 0, 8],
    9: [3, 6, 8, 6, 9, 1, 8, 4]
}

digit_idx_map = {
    0: [],
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: []
}
stones = []
with open("in.txt", "r") as in_f:
    for line in in_f:
        for c in line.strip().split(" "):
            stones.append(int(c))

start_ts = time.time()
prev_time = time.time()
blink_amount = 25
for i in range(blink_amount):
    print(f"{i} / {blink_amount}, SIZE: {len(stones)}, TIME: {time.time() - prev_time}")
    prev_time = time.time()
    
    stones = blink(stones)
    #stones = blink_v2(i, stones, digit_mapping, digit_idx_map)

print(f"{len(stones)}")