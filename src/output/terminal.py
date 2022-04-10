from src.game.game_of_life import makegrid, initialize, LIVE, DEAD, next_generation
import time

CHAR_LIVE = 'X'
CHAR_DEAD = ' '


def build_grid(grid):
    str_grid = ''
    for row in grid:
        str_grid += '\n'
        for field in row:
            str_grid += CHAR_LIVE if field == LIVE else CHAR_DEAD
    return str_grid


def main():
    grid = makegrid(columns=100, rows=50)
    grid = initialize(grid=grid)
    count = 0
    while True:
        time.sleep(0.1)
        print(build_grid(grid))
        count +=1
        grid = next_generation(grid=grid)
