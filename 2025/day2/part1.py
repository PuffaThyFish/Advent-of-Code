
def getBadIds(file_path):
    with open(file_path, 'r') as database:
        id_ranges = database.read().split(',')
        bad_ids = 0
        for id_range in id_ranges:        
            bad_ids += countBadIds(id_range)
    return bad_ids

def countBadIds(id_range):
    bad_ids_total = 0 
    split_index = id_range.find('-')
    lo = id_range[:split_index]
    hi = id_range[split_index+1:]
    for num in range(int(lo), int(hi)+1):
        num_len = len(str(num))
        if num_len == 1: continue
        midpoint = num_len//2
        if str(num)[:midpoint] == str(num)[midpoint:]:
            print(num)
            bad_ids_total += num
    return bad_ids_total


#print(countBadIds('10-22'))

print(getBadIds("2025\day2\input.txt"))