import copy

# returns coords [i, j]
def find_same_ants(i, j, map):
    ret_coords = []
    
    for l_i in range(0, len(map)):
        for l_j in range(0, len(map[i])):
            if(map[l_i][l_j] == map[i][j] and (i != l_i and j != l_j) ): # sus
                ret_coords.append([l_i, l_j])
    return ret_coords

def mark_antinodes(i, j, same_ant_coords, antinode_map):
    for coord_tup in same_ant_coords:        
        ant_i = i - (coord_tup[0] - i)
        ant_j = j - (coord_tup[1] - j)
        
        if(-1 < ant_i and ant_i < len(antinode_map) and -1 < ant_j and ant_j < len(antinode_map[0])):
            antinode_map[ant_i][ant_j] = "#"
            
def mark_antinodes_2(i, j, same_ant_coords, antinode_map):
    for coord_tup in same_ant_coords:
        #Forward
        res_harm_mult = 1
        while(-1 != res_harm_mult):
            ant_i = i - (coord_tup[0] - i) * res_harm_mult
            ant_j = j - (coord_tup[1] - j) * res_harm_mult
            
            if(-1 < ant_i and ant_i < len(antinode_map) and -1 < ant_j and ant_j < len(antinode_map[0])):
                antinode_map[ant_i][ant_j] = "#"
                res_harm_mult += 1
            else:
                res_harm_mult = -1
        
        #The antenna
        antinode_map[i][j] = "#"
        
        #Backwards
        res_harm_mult = -1
        while(1 != res_harm_mult):
            ant_i = i - (coord_tup[0] - i) * res_harm_mult
            ant_j = j - (coord_tup[1] - j) * res_harm_mult
            
            if(-1 < ant_i and ant_i < len(antinode_map) and -1 < ant_j and ant_j < len(antinode_map[0])):
                antinode_map[ant_i][ant_j] = "#"
                res_harm_mult -= 1
            else:
                res_harm_mult = 1

def find_ants(map, antinode_map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            same_ant_coords = []
            if(map[i][j] != "."):
                same_ant_coords = find_same_ants(i, j, map)
                mark_antinodes_2(i, j, same_ant_coords, antinode_map)

map = []
antinode_map = []
with open("in.txt", "r") as in_f:
    for line in in_f:
        line_arr = []
        ant_arr = []
        for c in line.strip():
            line_arr.append(c)
            ant_arr.append(".")
        map.append(line_arr)
        antinode_map.append(ant_arr)

find_ants(map, antinode_map)

count_ant = 0
for line in antinode_map:
    for c in line:
        if(c == "#"):
            count_ant += 1
print(count_ant)