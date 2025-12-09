import re

with open("input") as f:
    ranges = list[tuple[int, int]]()
    while True:
        line = f.readline().strip()
        if not line:
            break
        a, b = map(int, re.fullmatch("(\d+)-(\d+)", line).groups())
        ranges.append((a, b))
    result = 0
    while True:
        line = f.readline().strip()
        if not line:
            break
        n = int(line)
        if any(a <= n <= b for a, b in ranges):
            print(n, "fresh")
            result += 1
        else:
            print(n, "spoiled")
    print(result)
