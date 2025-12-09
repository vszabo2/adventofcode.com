from itertools import combinations
import numpy as np
from collections import deque
from collections.abc import Collection

def inclusive_range(i: int, j: int) -> slice:
    # return a slice including i, j, and all ints in between
    return slice(min(i, j), max(i, j) + 1)

def compress(numbers: Collection[int]) -> tuple[list[int | None], dict[int, int]]:
    l = [None]
    d = {}
    for i in sorted(numbers):
        d[i] = len(l)
        l.append(i)
        l.append(None)
    return l, d


def main() -> None:
    points = [[int(i) for i in line.strip().split(",")] for line in open("input")]
    x_index_to_value, x_value_to_index = compress({i for i, j in points})
    x_size = len(x_index_to_value)
    y_index_to_value = [None] + sorted({j for i, j in points}) + [None]
    y_value_to_index = {j: i for i, j in enumerate(y_index_to_value)}
    y_size = len(y_index_to_value)
    grid = np.ones((x_size, y_size), dtype=np.int8)
    # grid is all 1
    for (x1, y1), (x2, y2) in zip(points, points[1:] + [points[0]], strict=True):
        if x1 == x2:
            grid[x_value_to_index[x1], inclusive_range(y_value_to_index[y1], y_value_to_index[y2])] = 2
        elif y1 == y2:
            grid[inclusive_range(x_value_to_index[x1], x_value_to_index[x2]), y_value_to_index[y1]] = 2
        else:
            assert False
    # grid is all 1 except perimeter which is 2
    print(grid)
    queue = deque([(0, 0)])
    seen = {(0, 0)}
    while queue:
        x, y = queue.popleft()
        grid[x, y] = 0
        if x > 0 and grid[x-1, y] == 1 and (x-1, y) not in seen:
            queue.append((x-1, y))
            seen.add((x-1, y))
        if y > 0 and grid[x, y-1] == 1 and (x, y-1) not in seen:
            queue.append((x, y-1))
            seen.add((x, y-1))
        if x + 1 < x_size and grid[x+1, y] == 1 and (x+1, y) not in seen:
            queue.append((x+1, y))
            seen.add((x+1, y))
        if y + 1 < y_size and grid[x, y+1] == 1 and (x, y+1) not in seen:
            queue.append((x, y+1))
            seen.add((x, y+1))
    # grid has 2 on perimeter, 0 outside, and 1 inside
    print(grid)
    result = max(
        (abs(x2-x1) + 1) * (abs(y2-y1) + 1) 
        for (x1, y1), (x2, y2) in combinations(points, 2)
        if np.all(grid[
            inclusive_range(x_value_to_index[x1], x_value_to_index[x2]), 
            inclusive_range(y_value_to_index[y1], y_value_to_index[y2]),
        ])
    )
    print(result)


if __name__ == "__main__":
    main()
