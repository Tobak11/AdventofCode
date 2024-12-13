import re

# Part 1
l_dict = {
    "l" : [],
    "r": []
}

with open("in.txt", "r") as in_f:
    for line in in_f:
        tokens = re.split("\s+", line)
        l_dict["l"].append(tokens[0])
        l_dict["r"].append(tokens[1])

l_dict["l"].sort()
l_dict["r"].sort()

sum = 0
for i in range(len(l_dict["l"])):
    sum += abs(int(l_dict["r"][i]) - int(l_dict["l"][i]))
    
print(f'P1 {sum}')
    
# Part 2
count_dict = {}

for l_el in l_dict["l"]:
    if(l_el not in count_dict.keys()):
        count = 0
        for r_el in l_dict["r"]:
            if(l_el == r_el):
                count += 1
        
        if(0 != count):
            count_dict[l_el] = count
        
countSum = 0
for key in count_dict.keys():
    countSum += int(key) * int(count_dict[key])
    
print(f'P2 {countSum}')