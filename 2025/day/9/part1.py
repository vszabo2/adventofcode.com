from itertools import combinations

def main():
    points = [[int(i) for i in line.strip().split(",")] for line in open("input")]
    result = max((abs(x2-x1) + 1) * (abs(y2-y1) + 1) for (x1, y1), (x2, y2) in combinations(points, 2))
    print(result)


if __name__ == "__main__":
    main()
