def is_invalid(a: str) -> bool:
    b = len(a) // 2
    return a[:b] == a[b:]

def main(filename: str) -> int:
    result = 0
    for r in open(filename).read().strip().split(","):
        print(r)
        start, end = r.split("-")
        for i in range(int(start), int(end)+1):
            if is_invalid(str(i)):
                print(i)
                result += i
    return result

print("result", main("input"))
