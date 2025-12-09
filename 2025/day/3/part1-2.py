def f(s: str, start: int, end: int) -> int:
    """
    returns the index of the largest digit in the string, excluding indices outside of [start, end)
    """
    for i in reversed(range(10)):
        j = s.find(str(i), start, end)
        if j != -1:
            return j

def max_joltage(bank: str) -> int:
    j = f(bank, 0, len(bank)-1)
    l = f(bank, j+1, len(bank))
    return int(bank[j] + bank[l])

result = 0
for line in open("input"):
    i = max_joltage(line.strip())
    print(i)
    result += i
print("result", result)
