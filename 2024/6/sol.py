import copy
import time

def print_map(map):
    for line in map:
        print(line)
    print("")

class Guard:
    x: int
    y: int
    
    x_facing: int
    y_facing: int
    
    is_moving: bool
    
    #P2
    circle_coords: dict
    in_circle: int
    is_simulated: bool
    
    def __init__(self, x, y, x_facing, y_facing, is_simulated):
        self.x = x
        self.y = y
        self.x_facing = x_facing
        self.y_facing = y_facing
        self.is_moving = True
        
        #P2        
        self.circle_coords = {}
        self.circle_coords[(str(x) + str(y))] = 1
        
        self.in_circle = 0
        self.is_simulated = is_simulated
        
    def check_for_circle(self, xy_str, chk_val):       
        if(self.circle_coords[xy_str] == chk_val):
            self.in_circle = 1
            self.is_moving = False     
        
    def turn(self):
        if(self.x_facing == -1):
            self.x_facing = 0
            self.y_facing = -1
        elif(self.x_facing == 1):
            self.x_facing = 0
            self.y_facing = 1
        elif(self.y_facing == -1):
            self.y_facing = 0
            self.x_facing = 1
        elif(self.y_facing == 1):
            self.y_facing = 0
            self.x_facing = -1
            
    def step_forw(self, map):
        self.x = self.x + self.x_facing
        self.y = self.y + self.y_facing
        map[self.y][self.x] = "X"
                    
    def step(self, map):
        # Boundary check
        if(-1 == self.x + self.x_facing or self.x + self.x_facing == len(map[0])
           or
           -1 == self.y + self.y_facing or self.y + self.y_facing == len(map)
           ):
            self.is_moving = False
            return
        
        # Obstacle turn
        if(map[self.y + self.y_facing][self.x + self.x_facing] == "#" or map[self.y + self.y_facing][self.x + self.x_facing] == "$"):
            self.turn()
        else:
            self.step_forw(map)
            if(self.is_simulated):                
                xy_str = str(self.x) + str(self.y)
                if xy_str in self.circle_coords.keys():
                    self.circle_coords[xy_str] += 1
                else:
                    self.circle_coords[xy_str] = 1
                    
                self.check_for_circle(xy_str, 5)
                    
start_ts = time.time()
guard = None
with open("in.txt", "r") as in_f:
    empty_map = []
    orig_guard_pos = []
    
    map = []
    map_orig = []
    for i, line in enumerate(in_f):
        empty_arr = []
        c_arr = []
        for j, c in enumerate(line.strip()):
            empty_arr.append(".")
            if(c == "^"):
                guard = Guard(j, i, 0, -1, False)
                orig_guard_pos.append(i)
                orig_guard_pos.append(j)
                
                c_arr.append("X")
            else:
                c_arr.append(c)
        map.append(c_arr)
        empty_map.append(empty_arr)
    
    map_orig = copy.deepcopy(map)
    
    sim_guard_id = 0
    while(guard.is_moving):
        sim_guard_id += 1
        
        #P2
        map_sim = copy.deepcopy(map_orig)
        
        if((-1 < guard.x + guard.x_facing and guard.x + guard.x_facing < len(map[0]))
           and
           (-1 < guard.y + guard.y_facing and guard.y + guard.y_facing < len(map))
           and
           map_sim[guard.y + guard.y_facing][guard.x + guard.x_facing] != "#"):
            map_sim[guard.y + guard.y_facing][guard.x + guard.x_facing] = "$"
            
        #sim_guard = Guard(guard.x, guard.y, guard.x_facing, guard.y_facing, True, sim_guard_id)
        sim_guard = Guard(orig_guard_pos[1], orig_guard_pos[0], 0, -1, True)
        
        while(sim_guard.is_moving):            
            sim_guard.step(map_sim)
            
        if(sim_guard.in_circle and 
           not (guard.y + guard.y_facing == orig_guard_pos[0] and guard.x + guard.x_facing == orig_guard_pos[1])):
            empty_map[guard.y + guard.y_facing][guard.x + guard.x_facing] = "#"
        
        print(f"{sim_guard_id} / 6386")
        #print_map(map_sim)
        guard.step(map)
        
    #P1
    count_X = 0
    for line in map:
        for c in line:
            if(c == "X"):
                count_X += 1
    
    #P2
    emp_count = 0
    for line in empty_map:
        for c in line:
            if(c == "#"):
                emp_count += 1
                
    print(f"{emp_count}")
    print(f"Runtime: {time.time() - start_ts}")
    