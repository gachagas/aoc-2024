from collections import defaultdict
from dataclasses import dataclass


@dataclass(frozen=True)
class Coords:
    x: int
    y: int

    def __add__(self, other):
        return Coords(
            self.x + other.x,
            self.y + other.y,
        )


DIRECTIONS = [
    Coords(0, -1),
    Coords(1, 0),
    Coords(0, 1),
    Coords(-1, 0),
]

maps = {}
starting_points = []
for y, row in enumerate(input_.splitlines()):
    for x, cell in enumerate(row):
        height = int(cell)
        coord = Coords(x, y)
        maps[coord] = height
        if height == 0:
            starting_points.append(coord)


def solve_map(starts):
    paths = defaultdict(int)

    def solve_path(pos, height, start_pos):
        if height == 9:
            paths[(start_pos, pos)] += 1
            return
        for dir_ in DIRECTIONS:
            new_pos = pos + dir_
            if new_pos not in maps:
                continue
            new_height = maps[new_pos]
            if new_height != height + 1:
                continue
            solve_path(new_pos, new_height, start_pos)

    for start in starts:
        solve_path(start, 0, start)

    return paths


paths = solve_map(starting_points)
print("Part 1:", len(paths))
print("Part 2:", sum(paths.values()))
