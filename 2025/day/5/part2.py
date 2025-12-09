import bisect
import itertools
import re

def collapse_overlapping_inclusive_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    endpoints = list[int]() # even length. even indices are start points, odd indices are end points
    for a, b in ranges:
        i = bisect.bisect_left(endpoints, a)
        # If a equals an existing endpoint, push i inside the range
        if i < len(endpoints) and endpoints[i] == a:
            i += 1 ^ (i & 1)
        j = bisect.bisect_left(endpoints, b)
        if j < len(endpoints) and endpoints[j] == b:
        # If b equals an existing endpoint, push j inside the range
            j += 1 ^ (j & 1)

        if i & 1:
            # a is in the exising range endpoints[i-1]..endpoints[i]
            if j & 1:
                # b is in the existing range endpoints[j-1]..endpoints[j]
                endpoints[i:j] = []
            else:
                # b is between ranges, before endpoint[j]
                endpoints[i:j] = [b]

        else:
            # a is between ranges, after endpoint[i-1]
            if j & 1:
                # b is in the existing range endpoints[j-1]..endpoints[j]
                endpoints[i:j] = [a]
            else:
                # b is between ranges, before endpoint[j]
                endpoints[i:j] = [a, b]

    return [(endpoints[i], endpoints[i+1]) for i in range(0, len(endpoints), 2)]

def text_to_ranges(input: str) -> list[tuple[int, int]]:
    result = []
    for line in input.splitlines():
        line.strip()
        if not line:
            break
        a, b = map(int, re.fullmatch(r"(\d+)-(\d+)", line).groups())
        result.append((a, b))
    return result

def ranges_to_text(ranges: list[tuple[int, int]]) -> str:
    return "\n".join(f"{a}-{b}" for a, b in ranges)

def test(input, expected_output):
    actual_output = ranges_to_text(
        collapse_overlapping_inclusive_ranges(
            text_to_ranges(
                input
            )
        )
    )
    if actual_output != expected_output:
        print("Test Failed")
        print("Input")
        print(input)
        print("Actual Output")
        print(actual_output)
        print("Expected Output")
        print(expected_output)
        print("---")

test("", "")
test("5-10", "5-10")
test("""\
5-10
15-20""", """\
5-10
15-20""")
test("""\
15-20
5-10
25-30""",
"""\
5-10
15-20
25-30""")
test("""\
1-1
2-2
3-3
2-2""", """\
1-1
2-2
3-3""")
test("""\
5-10
15-20
7-17""", """\
5-20""")
test("""\
5-10
15-20
7-11""","""\
5-11
15-20""")
test("""\
10-11
10-11""", """\
10-11""")
test("""\
5-10
1-4
7-11""", """\
1-4
5-11""")
test("""\
5-10
15-20
11-15""","""\
5-10
11-20""")


with open("input") as f:
    file_contents = f.read()
text = file_contents[:file_contents.index("\n\n")]
print(sum(b - a + 1 for a, b in collapse_overlapping_inclusive_ranges(text_to_ranges(text))))
