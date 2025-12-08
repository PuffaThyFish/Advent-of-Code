
def getReachableRolls(file_path):
    with open(file_path, 'r') as warehouse:
        warehouse_grid = [list(row.strip()) for row in warehouse]
        reachable_rolls = findReachableRolls(warehouse_grid)
    return reachable_rolls

def findReachableRolls(warehouse_grid):
    reachable_rolls = 0
    for row in range(len(warehouse_grid)):
        for col in range(len(warehouse_grid[0])):
            if warehouse_grid[row][col] == '.': continue
            # dict of how many of what
            surroundings = checkSurroundings(warehouse_grid, row, col)
            if '@' not in surroundings or surroundings['@'] < 4:
                reachable_rolls += 1
    return reachable_rolls

def checkSurroundings(warehouse_grid, row, col):
    surroundings = dict()
    for row_modifier in (-1, 0, 1):
        for col_modifier in (-1, 0, 1):
            if (row_modifier, col_modifier) == (0, 0): continue
            new_row = row + row_modifier
            new_col = col + col_modifier
            if (new_row < 0 or new_row >= len(warehouse_grid) or 
                new_col < 0 or new_col >= len(warehouse_grid[0])): continue
            cell_value = warehouse_grid[new_row][new_col]
            if cell_value not in surroundings:
                surroundings[cell_value] = 1
            else:
                surroundings[cell_value] += 1
    return surroundings


#print(getReachableRolls(r"2025\day4\test.txt"))
print(getReachableRolls("2025\day4\input.txt"))