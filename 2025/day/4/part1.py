def main(filename: str) -> None:
    grid = [line.strip() for line in open(filename)]
    num_accessible = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "@":
                adjacent_rolls = 0
                for ii in range(-1, 2):
                    for jj in range(-1, 2):
                        if (ii, jj) != (0, 0) and 0 <= i+ii < len(grid) and 0 <= j+jj < len(grid[0]):
                            if i == 0 and j == 2:
                                print(f"{ii=} {jj=} {grid[i+ii][j+jj]=}")
                            if grid[i+ii][j+jj] == "@":
                                adjacent_rolls += 1
                            else:
                                assert grid[i+ii][j+jj] == "."

                if adjacent_rolls < 4:
                    num_accessible += 1
                print(f"{i=} {j=} {adjacent_rolls=}")
            else:
                assert grid[i][j] == "."
    print(num_accessible)

if __name__ == "__main__":
    main("input")
