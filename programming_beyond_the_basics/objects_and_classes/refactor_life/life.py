import os
import random
import time


class Cell:
    def __init__(self, state=False):
        self.state = state

    def is_alive(self):
        return self.state

    def set_state(self, state):
        self.state = state


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [[Cell() for _ in range(width)] for _ in range(height)]

    def get_cell(self, x, y):
        return self.cells[y][x]

    def set_cell(self, x, y, state):
        self.cells[y][x].set_state(state)


class GameOfLife:
    def __init__(self, width, height):
        self.grid = Grid(width, height)

    def initialize_random(self, probability=0.3):
        for y in range(self.grid.height):
            for x in range(self.grid.width):
                self.grid.set_cell(x, y, random.random() < probability)

    def step(self):
        new_grid = Grid(self.grid.width, self.grid.height)
        for y in range(self.grid.height):
            for x in range(self.grid.width):
                # cell = self.grid.get_cell(x, y)
                # neighbor_count = self.count_neighbors(x, y)
                # new_state = GameOfLife.apply_rules(cell, neighbor_count)
                new_state = self.apply_rules(x, y)
                new_grid.set_cell(x, y, new_state)
        self.grid = new_grid

    def run(self, iterations, delay=0.1):
        for _ in range(iterations):
            os.system('clear')  # Windows: os.system('cls')
            self.display()
            self.step()
            time.sleep(delay)

    def apply_rules(self, x, y):
        cell = self.grid.get_cell(x, y)
        neighbor_count = self.count_neighbors(x, y)

        if cell.is_alive():
            return 2 <= neighbor_count <= 3
        else:
            return neighbor_count == 3

    def count_neighbors(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = (x + dx) % self.grid.width, (y +
                                                      dy) % self.grid.height
                if self.grid.get_cell(nx, ny).is_alive():
                    count += 1
        return count

    def display(self):
        for y in range(self.grid.height):
            for x in range(self.grid.width):
                print('■' if self.grid.get_cell(
                    x, y).is_alive() else '□', end='')
            print()
        print()

    @staticmethod
    def run_game(width, height, iterations):
        game = GameOfLife(width, height)
        game.initialize_random()
        game.run(iterations)


if __name__ == "__main__":
    GameOfLife.run_game(50, 50, 50)
