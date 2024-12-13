import copy
import time

def path_step(i, j, th_str, isl_map, th_score_map, idx_arr):
    pos_str = str(i) + str(j)
    if(isl_map[j][i] == 9):
        if(th_str in th_score_map.keys()):
            if(pos_str not in th_score_map[th_str]):
                th_score_map[th_str].append(pos_str)
        else:
            th_score_map[th_str] = [pos_str]
        
        idx_arr.append([i, j])
        return
        
    left = i-1 
    right = i+1
    top = j-1
    bot = j+1
    if(-1 < left and isl_map[j][i] + 1 == isl_map[j][left]):
        path_step(left, j, th_str, isl_map, th_score_map, idx_arr)
    if(right < len(isl_map[0]) and isl_map[j][i] + 1 == isl_map[j][right]):
        path_step(right, j, th_str, isl_map, th_score_map, idx_arr)
    if(-1 < top and isl_map[j][i] + 1 == isl_map[top][i]):
        path_step(i, top, th_str, isl_map, th_score_map, idx_arr)
    if(bot < len(isl_map) and isl_map[j][i] + 1 == isl_map[bot][i]):
        path_step(i, bot, th_str, isl_map, th_score_map, idx_arr)

def traverse(isl_map, th_score_map, idx_arr):
    for j in range(len(isl_map)):
        for i in range(len(isl_map[0])):
            if(isl_map[j][i] == 0):
                th_str = str(i) + str(j)
                path_step(i, j, th_str, isl_map, th_score_map, idx_arr)
                
def th_score(th_score_map):
    count = 0
    
    for thsca_key in th_score_map.keys():
        count += len(th_score_map[thsca_key])
    return count

isl_map = []
th_score_map = {}
idx_arr = []
with open("in.txt", "r") as in_f:
    for i, line in enumerate(in_f):
        isl_map.append([])
        for c in line.strip():
            isl_map[i].append(int(c))
            
    traverse(isl_map, th_score_map, idx_arr)
    print(th_score(th_score_map))
    print(len(idx_arr))