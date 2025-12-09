def f(s: str, start: int, end: int) -> int:
    """
    returns the index of the largest digit in the string, excluding indices outside of [start, end)
    """
    for i in reversed(range(10)):
        j = s.find(str(i), start, end)
        if j != -1:
            return j

def max_joltage(bank: str) -> int:
    result = ""
    start = 0
    l = len(bank)
    for i in range(12):
        j = f(bank, start, len(bank) - 11 + i)
        result += bank[j]
        start = j + 1
    return int(result)

result = 0
for line in open("input"):
    i = max_joltage(line.strip())
    print(i)
    result += i
print("result", result)
