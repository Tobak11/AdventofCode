import re

with open("in.txt", "r") as in_f:
    str_dump = in_f.read()
    mul_list = re.findall("(mul\(\d+\,\d+\)|do\(\)|don't\(\))", str_dump)
    
    append_flag = True
    mul_list_filtered = []
    for el in mul_list:
        if(el == "do()"): append_flag = True
        elif(el == "don't()"): append_flag = False
        else:
            if(append_flag):
                mul_list_filtered.append(el)
    
    res = 0
    for el in mul_list_filtered:
        el = re.sub("mul\(", "", el)
        el = re.sub("\)", "", el)
        d_tok = el.split(",")
        
        res += int(d_tok[0]) * int(d_tok[1])
        
    print(res)