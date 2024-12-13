import copy
import time

def get_perim(perim_calc_mask):
    perim_count = 0
    for y in range(len(perim_calc_mask)):
        for x in range(len(perim_calc_mask[0])):
            if(perim_calc_mask[y][x] == 1):
                #T
                if(-1 < y - 1):
                    if perim_calc_mask[y-1][x] == 0:
                        perim_count += 1
                else:
                    perim_count += 1
                    
                #B 
                if y + 1 < len(perim_calc_mask): 
                    if perim_calc_mask[y+1][x] == 0:
                        perim_count += 1
                else:
                    perim_count += 1
                    
                #L
                if(-1 < x - 1): 
                    if perim_calc_mask[y][x-1] == 0:
                        perim_count += 1
                else:
                    perim_count += 1
                    
                #R
                if(x + 1 < len(perim_calc_mask[0])):
                    if perim_calc_mask[y][x+1] == 0:
                        perim_count += 1
                else:
                    perim_count += 1
                    
    return perim_count

def count_sides(side_dict):
    side_count = 0
    for key in side_dict.keys():
        side_group_idx = 0
        side_groups = [[side_dict[key][0]]]
        for i in range(1, len(side_dict[key])):
            if(side_dict[key][i - 1] != side_dict[key][i] - 1):
                side_groups.append([])
                side_group_idx += 1
            side_groups[side_group_idx].append(side_dict[key][i])
        side_count += len(side_groups)
                
    return side_count

def get_perim_v2(perim_calc_mask):
    top_dict = {}
    bot_dict = {}
    left_dict = {}
    right_dict = {}
    for y in range(len(perim_calc_mask)):
        for x in range(len(perim_calc_mask[0])):
            if(perim_calc_mask[y][x] == 1):
                #T
                if(-1 < y - 1):
                    if perim_calc_mask[y-1][x] == 0:
                        if(y in top_dict.keys()):
                            if(x not in top_dict[y]):
                                top_dict[y].append(x)
                        else:
                            top_dict[y] = [x]
                else:
                    if(y in top_dict.keys()):
                        if(x not in top_dict[y]):
                            top_dict[y].append(x)
                    else:
                        top_dict[y] = [x]
                    
                #B 
                if y + 1 < len(perim_calc_mask): 
                    if perim_calc_mask[y+1][x] == 0:
                        if(y in bot_dict.keys()):
                            if(x not in bot_dict[y]):
                                bot_dict[y].append(x)
                        else:
                            bot_dict[y] = [x]
                else:
                    if(y in bot_dict.keys()):
                        if(x not in bot_dict[y]):
                            bot_dict[y].append(x)
                    else:
                        bot_dict[y] = [x]
                    
                #L
                if(-1 < x - 1): 
                    if perim_calc_mask[y][x-1] == 0:
                        if(x in left_dict.keys()):
                            if(y not in left_dict[x]):
                                left_dict[x].append(y)
                        else:
                            left_dict[x] = [y]
                else:
                    if(x in left_dict.keys()):
                        if(y not in left_dict[x]):
                            left_dict[x].append(y)
                    else:
                        left_dict[x] = [y]
                    
                #R
                if(x + 1 < len(perim_calc_mask[0])):
                    if perim_calc_mask[y][x+1] == 0:
                        if(x in right_dict.keys()):
                            if(y not in right_dict[x]):
                                right_dict[x].append(y)
                        else:
                            right_dict[x] = [y]
                else:
                    if(x in right_dict.keys()):
                        if(y not in right_dict[x]):
                            right_dict[x].append(y)
                    else:
                        right_dict[x] = [y]
                    
    return count_sides(top_dict) + count_sides(bot_dict) + count_sides(left_dict) + count_sides(right_dict)
                
def get_region_total(base_map, proc_mask, perim_calc_mask, y, x):
    pcm_loc = copy.deepcopy(perim_calc_mask)
    plant_to_look = base_map[y][x]
    check_neigh_arr = [[y, x]]
    in_reg_processed = []
    while(len(check_neigh_arr) > 0):
        curr_pos = check_neigh_arr[0]
        if(-1 < curr_pos[0] - 1 and base_map[curr_pos[0] - 1][curr_pos[1]] == plant_to_look):
            temp_arr = [curr_pos[0] - 1, curr_pos[1]]
            if(temp_arr not in in_reg_processed and temp_arr not in check_neigh_arr):
                check_neigh_arr.append([curr_pos[0] - 1, curr_pos[1]])
        if(curr_pos[0] + 1 < len(base_map) and base_map[curr_pos[0] + 1][curr_pos[1]] == plant_to_look):
            temp_arr = [curr_pos[0] + 1, curr_pos[1]]
            if(temp_arr not in in_reg_processed and temp_arr not in check_neigh_arr):
                check_neigh_arr.append(temp_arr)
        if(-1 < curr_pos[1] - 1 and base_map[curr_pos[0]][curr_pos[1] - 1] == plant_to_look):
            temp_arr = [curr_pos[0], curr_pos[1] - 1]
            if(temp_arr not in in_reg_processed and temp_arr not in check_neigh_arr):
                check_neigh_arr.append(temp_arr)
        if(curr_pos[1] + 1 < len(base_map[0]) and base_map[curr_pos[0]][curr_pos[1] + 1] == plant_to_look):
            temp_arr = [curr_pos[0], curr_pos[1] + 1]
            if(temp_arr not in in_reg_processed and temp_arr not in check_neigh_arr):
                check_neigh_arr.append(temp_arr)
        
        if(check_neigh_arr[0] not in in_reg_processed):
            proc_mask[curr_pos[0]][curr_pos[1]] = 1
            pcm_loc[curr_pos[0]][curr_pos[1]] = 1
            in_reg_processed.append(check_neigh_arr[0])
        del check_neigh_arr[0]
    
    return len(in_reg_processed) * get_perim_v2(pcm_loc)
            

def traverse_base_map(base_map, proc_mask, perim_calc_mask):
    map_total = 0
    for y in range(len(base_map)):
        for x in range(len(base_map[0])):
            if(proc_mask[y][x] == 0):
                map_total += get_region_total(base_map, proc_mask, perim_calc_mask, y, x)
    return map_total
        
base_map = []
proc_mask = []
perim_calc_mask = []
with open("in.txt", "r") as in_f:
    for line in in_f:
        base_map_row = []
        pm_row = []
        pc_row = []
        for c in line.strip():
            base_map_row.append(c)
            pm_row.append(0)
            pc_row.append(0)
        base_map.append(base_map_row)
        proc_mask.append(pm_row)
        perim_calc_mask.append(pc_row)

print(traverse_base_map(base_map, proc_mask, perim_calc_mask))