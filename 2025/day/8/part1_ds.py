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
    for _, a, b in distances[:1000]:
        # print("linking {} and {}".format(positions[a], positions[b]))
        i = disjoint_set_lookup(disjoint_sets, a)
        j = disjoint_set_lookup(disjoint_sets, b)
        if i != j:
            target_set = min(i, j)
            disjoint_sets[i] = disjoint_sets[j] = target_set
            # print(target_set)

    print(math.prod(count for _, count in Counter(
        disjoint_set_lookup(disjoint_sets, i) for i in range(len(disjoint_sets))
    ).most_common(3)))

if __name__ == "__main__":
    main()
