from itertools import count

def start_entry_to_beam(s: str) -> bool:
    match s:
        case "S":
            return True
        case ".":
            return False
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

beams = list[bool]()
result = 0
for line in open("input"):
    if beams:
        for i, (has_beam, reached_splitter) in enumerate(zip(
            beams, 
            map(splitter_line_character, line.strip()), 
            strict=True,
        )):
            if has_beam and reached_splitter:
                beams[i-1:i+2] = [True, False, True]
                result += 1
    else:
        # first row
        beams = [start_entry_to_beam(c) for c in line.strip()]
print(result)
