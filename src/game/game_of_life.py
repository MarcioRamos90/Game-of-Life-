from random import choice

LIVE = 1
DEAD = 0

ROWS = 20
COLUMNS = 20


def initialize(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            value_field = choice([LIVE, DEAD])
            grid[row][col] = value_field
    return grid


def makegrid(columns, rows):
    return [[DEAD for _ in range(columns)] for _ in range(rows)]


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


def next_generation(grid,**kargs):
        next_grid = [r.copy() for r in grid]
        qtd_cols = len(grid[0])
        qtd_rows = len(grid)

        for row in range(0, len(grid)):
            for col in range(0, len(grid[row])):
                qtd_n = qtd_live_neighbors(
                    grid=grid, col=col, row=row, len_col=qtd_cols, len_row=qtd_rows
                )
                if qtd_n == 3:
                    next_grid[row][col] = LIVE 
                elif qtd_n == 2 and grid[row][col] == LIVE:
                    next_grid[row][col] = LIVE
                elif qtd_n < 2 or qtd_n > 3:
                    next_grid[row][col] = DEAD
        return next_grid
    