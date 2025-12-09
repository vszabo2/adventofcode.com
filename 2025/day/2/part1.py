from sympy import divisors

def is_invalid(a: str) -> bool:
    l = len(a)
    for repeat_len in divisors(l)[:-1]:
        if a == a[:repeat_len] * (l // repeat_len):
            return True

def main(filename: str) -> int:
    result = 0
    for r in open(filename).read().strip().split(","):
        # print(r)
        start, end = r.split("-")
        for i in range(int(start), int(end)+1):
            if is_invalid(str(i)):
                # print(i)
                result += i
    return result

print("result", main("input"))
