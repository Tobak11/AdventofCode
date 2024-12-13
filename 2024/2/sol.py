import re

safe_c = 0
with open("in.txt", "r") as in_f:
    for line in in_f:        
        in_arr = list(map(int, filter(None, re.split("\s+", line))))
        damp_arrs = []
        for i in range(len(in_arr)):
            arr_cpy = in_arr.copy()
            del arr_cpy[i]
            damp_arrs.append(arr_cpy)
        
        sol_found = False
        for damp_arr in damp_arrs:
            if(sol_found):
                break
            
            flag_arr = [True, True, True] # ASC, DESC, RANGE
            prev = -1
            for el in damp_arr:
                if(-1 == prev):
                    prev = el
                else:
                    # Range check
                    diff_val = abs(el-prev)
                    if(not(1 <= diff_val and diff_val <=3)):
                        flag_arr[2] = False
                    
                    # ASC check    
                    if(el <= prev):
                        flag_arr[0] = False
                        
                    # DESC check    
                    if(prev <= el):
                        flag_arr[1] = False
                        
                    # Set prev for next IT
                    prev = el
            
            if((flag_arr[0] or flag_arr[1]) and flag_arr[2]):
                safe_c += 1
                sol_found = True
            
print(safe_c)