import re

in_arr = [] # Char matrix
line_arr = [] # Lines to eval


def vertical():
    for i in range(len(in_arr[0])): # Col
        str_build = ""
        for j in range(len(in_arr)): # Row
            str_build += in_arr[j][i]
            
        line_arr.append(str_build) # T -> B
        line_arr.append(str_build[::-1]) # B -> T
        
def diagonal():
    dr_start_coords = [] # Down Right -> [i, j], i: row, j: col
    dl_start_coords = [] # Down Left -> [i, j], i: row, j: col
    
    # Add first col to DR start coords
    for i in range(len(in_arr)):
        dr_start_coords.append([i, 0])
        
    # Add first col to DL start coords
    for i in range(len(in_arr)):
        dl_start_coords.append([i, len(in_arr[0]) - 1])
    
    # Add top row to DR start coords
    for j in range(1, len(in_arr[0])): # Start from 1 to not double add the big diag
        dr_start_coords.append([0, j])
        
    # Add top row to DL start coords
    for j in range(0, len(in_arr[0]) - 1): # Start from 1 to not double add the big diag
        dl_start_coords.append([0, j])
    
    # Adding DR strings to line_arr
    for sc in dr_start_coords:
        str_build = ""
        
        i = sc[0] 
        j = sc[1]
        while(i < len(in_arr[0]) and j < len(in_arr)):
            str_build += in_arr[j][i]
            
            i += 1
            j += 1
        
        if(4 <= len(str_build)):
            line_arr.append(str_build) # TL -> BR
            line_arr.append(str_build[::-1]) # BR -> TL
    
    # Adding DL strings to line_arr
    for sc in dl_start_coords:
        str_build = ""
        
        i = sc[0] 
        j = sc[1]
        while(i < len(in_arr[0]) and 0 <= j ):
            str_build += in_arr[j][i]
            
            i += 1
            j -= 1
        
        if(4 <= len(str_build)):
            line_arr.append(str_build) # TR -> BL
            line_arr.append(str_build[::-1]) # BL -> TR

def count_XMAS():
    count = 0
    for line in line_arr:
        count += len(re.findall("XMAS", line))
    print(count)
    
def count_X_MAS():
    count = 0
    
    A_coords = [] # [i, j], i: row, j: col
    for i in range(1, len(in_arr[0]) - 1): # Col
        for j in range(1, len(in_arr) - 1): # Row
            if(in_arr[j][i] == 'A'):
                A_coords.append([i, j])
                
    for A_c in A_coords:
        tl = in_arr[A_c[1] - 1][A_c[0] - 1]
        br = in_arr[A_c[1] + 1][A_c[0] + 1]
        
        tr = in_arr[A_c[1] - 1][A_c[0] + 1]
        bl = in_arr[A_c[1] + 1][A_c[0] - 1]
        
        if( ((tl == "S" and br == "M") or (tl == "M" and br == "S")) and ((tr == "S" and bl == "M") or (tr == "M" and bl == "S")) ):
            count += 1
    
    print(count)
    
with open("in.txt", "r") as in_f:
    for line in in_f:
        line = line.strip()
        
        char_arr = []
        for c in line:
            char_arr.append(c)
        in_arr.append(char_arr)
        
        # Horizontal
        line_arr.append(line) # L -> R
        line_arr.append(line[::-1]) # R -> L
    
    # Character based assembly
    vertical()
    diagonal()
    count_XMAS()
    
    count_X_MAS()