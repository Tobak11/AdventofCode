import re
import time

rule_map = {}
order_arr = []

def rulecheck(i, order):
    rule_vals = get_rule_vals(order[i])
    for rule in rule_vals: 
        for j in range(len(order)):
            if(order[j] == rule):
                if(i>j):
                    return True
    
    return False

def get_rule_vals(val):
    if(val in rule_map.keys()):
        return rule_map[val]
    else:
        return []

def rulecheck_idx(order):
    for i in range(len(order)):
        rule_vals = get_rule_vals(order[i])
        for rule in rule_vals: 
            for j in range(i - 1, -1, -1):
                if(order[j] == rule):
                    if(i>j):
                        return [i, j]
    return [-1, -1]

def fix(order):
    j = -2
    while(j != -1):
        i, j = rulecheck_idx(order)
        temp = order[i]
        order[i] = order[j]
        order[j] = temp
    
    return order

start_ts = time.time()
with open("in.txt", "r") as in_f:
    for line in in_f:
        cl_line = line.strip()
        
        if("|" in cl_line):
            tokens = cl_line.split("|")
            
            if(tokens[0] in rule_map.keys()):
                rule_map[tokens[0]].append(tokens[1])
            else:
                rule_map[tokens[0]] = [tokens[1]]
        else:
            tokens = cl_line.split(",")
            if(2 < len(tokens)):
                order_arr.append(cl_line.split(","))
            
    # Check
    p1_sol = 0
    p2_sol = 0
    for order in order_arr:
        violated_flag = False
        for i in range(len(order)):
            violated_flag = rulecheck(i, order)
            if(violated_flag == True):
                break
                
        if(not violated_flag):
            p1_sol += int(order[int((len(order) - 1)/2)])
        else:
            order_fixed = fix(order)
            p2_sol += int(order_fixed[int((len(order_fixed) - 1)/2)])
            
    print(p1_sol)
    print(p2_sol)
    
print(f"Runtime {time.time() - start_ts} s")