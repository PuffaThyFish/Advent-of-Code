
def getReachableRolls(file_path):
    with open(file_path, 'r') as warehouse:
        warehouse_grid = [list(row.strip()) for row in warehouse]
        reachable_rolls = 0
        prevRolls = 0
        curRolls = None
        while curRolls != prevRolls:
            printGrid(warehouse_grid)
            print('~~~~~~~~~~~~~~~~~')
            findReachableRolls(warehouse_grid) # marks with an 'X'
            grabbed = grabReachableRolls(warehouse_grid) # turns 'X' into '.'
            reachable_rolls += grabbed
            prevRolls = curRolls
            curRolls = countRolls(warehouse_grid)
    return reachable_rolls

def findReachableRolls(warehouse_grid):
    for row in range(len(warehouse_grid)):
        for col in range(len(warehouse_grid[0])):
            if warehouse_grid[row][col] == '.': continue
            # dict of how many of what
            surroundings = checkSurroundings(warehouse_grid, row, col)
            nearby = 0
            if 'X' in surroundings:
                nearby += surroundings['X']
            if '@' in surroundings:
                nearby += surroundings['@']
            
            if nearby < 4:
                warehouse_grid[row][col] = 'X'

def grabReachableRolls(warehouse_grid):
    grabbed = 0
    for row in range(len(warehouse_grid)):
        for col in range(len(warehouse_grid[0])):
            if warehouse_grid[row][col] == 'X':
                warehouse_grid[row][col] = '.'
                grabbed += 1
    return grabbed


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

def countRolls(warehouse_grid):
    rolls = 0
    for row in range(len(warehouse_grid)):
        for col in range(len(warehouse_grid[0])):
            if warehouse_grid[row][col] == '@':
                rolls += 1
    return rolls

def printGrid(grid):
    for row in grid:
        print(''.join(row))

print(getReachableRolls(r"2025\day4\test.txt"))
print(getReachableRolls("2025\day4\input.txt"))