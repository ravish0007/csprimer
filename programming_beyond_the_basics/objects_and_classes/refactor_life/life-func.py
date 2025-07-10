
import os
import random
import time
from pprint import pprint

random.seed(42)


def make_grid(length, breadth):
    grid = []
    for _ in range(length):
        grid.append([0 for _ in range(breadth)])
    return grid


def randomize_grid(grid, probability=0.3):
    randomized_grid = []
    for row in grid:
        new_row = [random.random() < probability for _ in range(len(row))]
        randomized_grid.append(new_row)
    return randomized_grid


def display(grid):
    for y in range(len(grid)):
        for x in grid[y]:
            print('■' if x else '□', end='')
        print()
    print()


def is_cell_alive(x): return x


def count_neighbors(grid, x, y):
    grid_width = len(grid[0])
    grid_height = len(grid)
    count = 0

    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = (x + dx) % grid_width, (y + dy) % grid_height
            if is_cell_alive(grid[nx][ny]):
                count += 1
    return count


def apply_rules(grid, x, y):
    cell = grid[x][y]
    neighbor_count = count_neighbors(grid, x, y)

    if is_cell_alive(cell):
        return 2 <= neighbor_count <= 3
    else:
        return neighbor_count == 3


def step(grid):
    grid_width = len(grid[0])
    grid_height = len(grid)
    new_grid = make_grid(len(grid), len(grid[0]))

    for y in range(grid_height):
        for x in range(grid_width):
            new_state = apply_rules(grid, x, y)
            new_grid[x][y] = new_state
    return new_grid


def run(grid, iterations, delay=0.1):
    for _ in range(iterations):
        os.system('clear')
        display(grid)
        grid = step(grid)
        time.sleep(delay)


def run_game(width, height, iterations):
    grid = make_grid(width, height)
    grid = randomize_grid(grid)
    run(grid, iterations)


if __name__ == "__main__":
    run_game(50, 50, 5)
