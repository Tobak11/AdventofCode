import copy
import time

def generate_disk_map(in_str, disk_map):
    runn_id = 0
    file_flag = True
    
    for c in in_str:
        if file_flag == True:
            for _ in range(int(c)):
                disk_map.append(runn_id)
            runn_id += 1
        else:
            for _ in range(int(c)):
                disk_map.append(".")
        file_flag = not file_flag
        
def compress(disk_map):
    max_num_idx = len(disk_map) - 1
    for es_i in range(0, len(disk_map)):
        if(disk_map[es_i] == "."):
            for loc_max_i in range(max_num_idx, -1, -1):
                if(loc_max_i <= es_i):
                    es_i = len(disk_map)
                    return
                
                if(disk_map[loc_max_i] != "."):
                    disk_map[es_i] = disk_map[loc_max_i]
                    disk_map[loc_max_i] = "."
                    break

def get_next_es(look_block_len, look_max_idx, disk_map):
    idx = 0
    while(idx < look_max_idx):
        if(disk_map[idx] == "."):
            block_len = 1
            bf_idx = idx + 1
            ses_flag = True
            while(ses_flag and bf_idx < len(disk_map)):
                if(disk_map[idx] == disk_map[bf_idx]):
                    block_len += 1
                    bf_idx += 1
                else:
                    ses_flag = False
            
            if block_len >= look_block_len:
                return idx
            else:
                idx = bf_idx
        else:
            idx += 1
    return -1
                          
def compress_2(disk_map):
    max_num_idx = len(disk_map) - 1
    while(-1 < max_num_idx):
        if(disk_map[max_num_idx] != "."):
            # Find num block
            block_len = 1
            nf_idx = max_num_idx - 1
            sn_flag = True
            while(sn_flag == True and -1 < nf_idx):
                if(disk_map[max_num_idx] == disk_map[nf_idx]):
                    block_len += 1
                    nf_idx -= 1
                else:
                    sn_flag = False

            #Check for empty space
            es_idx = get_next_es(block_len, max_num_idx - block_len + 1, disk_map)
            #Write it into place
            if(-1 != es_idx):
                print(max_num_idx)
                # Write into new space
                for i in range(es_idx, es_idx + block_len):
                    disk_map[i] = disk_map[max_num_idx]
                # Empty old space
                for i in range(max_num_idx - block_len + 1, max_num_idx + 1):
                    disk_map[i] = "."
                
            max_num_idx = nf_idx
        else:
            max_num_idx -= 1

def calc_checksum(disk_map):
    checksum = 0
    idx = 0
    while(idx < len(disk_map)):
        if(disk_map[idx] != "."):
            checksum += int(disk_map[idx]) * idx
        idx += 1
    return checksum
        
in_str = None
disk_map = []
with open("in.txt", "r") as in_f:
    in_str = in_f.read().strip()
    
    start_ts = time.time()
    generate_disk_map(in_str, disk_map)
    compress_2(disk_map)
    print(calc_checksum(disk_map))
    end_ts = time.time()
    
    print(f"Runtime: {end_ts-start_ts}")
    
    """
    start_ts = time.time()
    in_str = in_f.read()
    read_ts = time.time()
    
    generate_disk_map(in_str, disk_map)
    gen_ts = time.time()
    compress(disk_map)
    comp_ts = time.time()
    print(calc_checksum(disk_map))
    chksum_ts = time.time()
    
    print(f"read_ts: {read_ts-start_ts}")
    print(f"gen_ts: {gen_ts-start_ts}")
    print(f"comp_ts: {comp_ts-start_ts}")
    print(f"chksum_ts: {chksum_ts-start_ts}")
    """