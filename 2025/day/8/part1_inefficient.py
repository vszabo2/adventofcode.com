import math
import numpy as np

def lookup(s: set[set[int]], a: int) -> set[int]:
    for i in s:
        if a in i:
            return i

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
    groups = {frozenset((i,)) for i in range(len(positions))}
    num_links = 0
    for _, a, b in distances[:1000]:
        # print("linking {} and {}".format(positions[a], positions[b]))
        i = lookup(groups, a)
        j = lookup(groups, b)
        if i is not j:
            groups.remove(i)
            groups.remove(j)
            groups.add(i | j)
            # num_links += 1
            # if num_links == 10:
            #     break
    # else:
    #     assert False

    print(groups)
    # print(sorted((len(group) for group in groups), reverse=True)[:3])
    print(math.prod(sorted((len(group) for group in groups), reverse=True)[:3]))

if __name__ == "__main__":
    main()
