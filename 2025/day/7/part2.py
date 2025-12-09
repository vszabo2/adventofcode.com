from itertools import count

def start_entry_to_timelines(s: str) -> int:
    match s:
        case "S":
            return 1
        case ".":
            return 0
        case _:
            assert False

def splitter_line_character(s: str) -> bool:
    match s:
        case "^":
            return True
        case ".":
            return False
        case _:
            assert False

num_timelines = list[int]()
for line in open("input"):
    if num_timelines:
        next_num_timelines = [0] * h
        for i in range(h):
            if splitter_line_character(line[i]):
                next_num_timelines[i-1] += num_timelines[i]
                next_num_timelines[i+1] += num_timelines[i]
            else:
                next_num_timelines[i] += num_timelines[i]
        num_timelines = next_num_timelines
    else:
        # first row
        num_timelines = [start_entry_to_timelines(c) for c in line.strip()]
        h = len(num_timelines)
print(sum(num_timelines))
