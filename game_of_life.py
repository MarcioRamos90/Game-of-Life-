from random import choice

LIVE = 1
DEAD = 0

ROWS = 20
COLUMNS = 20


def initialize(grid):
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            value_field = choice([LIVE, DEAD])
            grid[x][y] = value_field
    return grid


def makegrid(columns, rows):
    return [[0]*columns] * rows


def qtd_live_neighbors(grid, col, row, len_col, len_row):
    neighbors_sum = 0
    for x in range(-1, 2):
        for y in range(-1, 2):
            neighbors_sum += grid[x + row][y + col]
    
    neighbors_sum -= grid[row][col]
    return neighbors_sum


# TODO:finish logic
def next_generation(grid):
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if qtd_live_neighbors(grid=grid, col=x, row=y) == 3:
                grid[x][y] = LIVE
    return grid
