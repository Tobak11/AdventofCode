import copy

def calc_step(big_op, small_op, oper):
    if(oper == "+"):
        return big_op + small_op
    if(oper == "*"):
        return big_op * small_op
    if(oper == "|"):
        return int(str(big_op) + str(small_op))
        
def get_oper_combos(noc, opers):
    prev_leaves = []
    leaf_combos = []
    
    for i in range(noc):
        if(len(leaf_combos) == 0):
            for oper in opers:
                leaf_combos.append([oper])
        else:
            leaf_combos = []
            for prev_leaf in prev_leaves:
                for oper in opers:
                    temp_arr = copy.deepcopy(prev_leaf)
                    temp_arr.append(oper)
                    leaf_combos.append(temp_arr)
        prev_leaves = leaf_combos
    return leaf_combos

def brutality(num, vals, opers):
    combos = get_oper_combos(len(vals) - 1, opers)
    
    for combo in combos:
        poss_num = vals[0]
        for i, oper in enumerate(combo):
            poss_num = calc_step(poss_num, vals[i+1], oper)
            
        if(poss_num == num):
            return poss_num
        
    all_mult = vals[0]
    for i in range(1, len(vals)):
        all_mult *= vals[i]
    
    return 0

opers = ["+", "*", "|"]
with open("in.txt", "r") as in_f:
    total_calib_res = 0
    for i, line in enumerate(in_f):
        if(i % 10 == 0):
            print(i)
            
        num = int(line.split(":")[0])
        in_arr = []
        
        for val in line.split(":")[1].strip().split(" "):
            in_arr.append(int(val))
            
        brut_val = brutality(num, in_arr, opers)
        total_calib_res += brut_val

    print(total_calib_res)