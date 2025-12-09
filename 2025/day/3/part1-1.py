def max_joltage(bank: str) -> int:
    prebank = bank[:-1]
    for i in reversed(range(10)):
        j = prebank.find(str(i))
        if j != -1:
            postbank = bank[j+1:]
            for k in reversed(range(10)):
                l = postbank.find(str(k))
                if l != -1:
                    return int(prebank[j] + postbank[l])

result = 0
for line in open("input"):
    i = max_joltage(line.strip())
    print(i)
    result += i
print("result", result)
