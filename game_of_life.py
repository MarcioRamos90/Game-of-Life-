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
    return [[0] * columns] * rows


def qtd_live_neighbors(grid, col, row, len_col, len_row):
    try:
        neighbors_sum = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                neighbor_col = (x + col) % len_col
                neighbor_row = (y + row) % len_row
                neighbors_sum += grid[neighbor_row][neighbor_col]

        neighbors_sum -= grid[row][col]
        return neighbors_sum
    except IndexError:
        print(f"out of index x:{neighbor_col} y:{neighbor_row}")
        raise


def next_generation(grid, len_col, len_row):
        next_grid = [r.copy() for r in grid]
        for row in range(0, len_row):
            for col in range(0, len_col):
                print(dict(row=row, col=col, value=grid[row][col]))
                qtd_n = qtd_live_neighbors(
                    grid=grid, col=col, row=row, len_col=len_col, len_row=len_row
                )
                if qtd_n == 3:
                    next_grid[row][col] = LIVE 
                elif qtd_n == 2 and grid[row][col] == LIVE:
                    next_grid[row][col] = LIVE
                elif qtd_n < 2 or qtd_n > 3:
                    next_grid[row][col] = DEAD
        return next_grid
    