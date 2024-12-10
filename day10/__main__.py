from pathlib import Path
from typing import List
from collections import deque


def load_input():
    input_path = Path(__file__).parent / "input.txt"
    arr = []
    with open(input_path, "r") as f:
        while line := f.readline():
            line = line.strip()
            arr.append([int(x) if x != "." else -1 for x in line])

    return arr


def traverse_trailhead(
    grid: dict[tuple[int, int], int],
    pos: tuple[int, int],
    grid_width: int,
    grid_height: int,
):
    trailhead_score = 0
    reached_nines = set()

    queue = deque()
    visited = set()

    queue.append((pos, 0))  # position, current height
    visited.add(pos)

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # right down left up

    while queue:
        curr_pos, curr_height = queue.popleft()

        for dx, dy in directions:
            new_x = curr_pos[0] + dx
            new_y = curr_pos[1] + dy
            next_pos = (new_x, new_y)

            if 0 <= new_x < grid_width and 0 <= new_y < grid_height:
                if next_pos in visited:
                    continue

                if grid.get(next_pos) == -1:
                    continue

                if grid[next_pos] == curr_height + 1:
                    if grid[next_pos] == 9 and next_pos not in reached_nines:
                        trailhead_score += 1
                        reached_nines.add(next_pos)
                    queue.append((next_pos, grid[next_pos]))
                    visited.add(next_pos)

    return trailhead_score


def main():
    data: List[List[int]] = load_input()

    grid_height = len(data)
    grid_width = len(data[0])
    grid = {(x, y): data[y][x] for x in range(grid_width) for y in range(grid_height)}

    trail_score = 0
    for pos, height in grid.items():
        if height == 0:
            trailhead_score = traverse_trailhead(
                grid=grid, pos=pos, grid_width=grid_width, grid_height=grid_height
            )
            trail_score = trail_score + trailhead_score

    print(trail_score)


if __name__ == "__main__":
    main()
