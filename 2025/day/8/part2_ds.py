from collections import Counter
import math
import numpy as np

def disjoint_set_lookup(disjoint_sets: list[int], a: int) -> int:
    if disjoint_sets[a] == a:
        return a
    r = disjoint_set_lookup(disjoint_sets, disjoint_sets[a])
    assert r < a
    disjoint_sets[a] = r
    return r

def main() -> None:
    positions = [np.array(tuple(map(int, line.strip().split(",")))) for line in open("input")]
    distances = sorted(
        (
            np.linalg.norm(positions[i] - positions[j]),
            i,
            j,
        )
        for i in range(len(positions) - 1)
        for j in range(i+1, len(positions))
    )
    disjoint_sets = list(range(len(positions)))
    num_sets = 1000
    for _, a, b in distances:
        # print("linking {} and {}".format(positions[a], positions[b]))
        i = disjoint_set_lookup(disjoint_sets, a)
        j = disjoint_set_lookup(disjoint_sets, b)
        if i != j:
            target_set = min(i, j)
            disjoint_sets[i] = disjoint_sets[j] = target_set
            # print(target_set)
            num_sets -= 1
            if num_sets == 1:
                print(positions[a][0] * positions[b][0])


if __name__ == "__main__":
    main()
