result = 0
a = 50
for line in open("input.txt"):
    dir = line[0]
    num = int(line[1:])
    result += num // 100
    num %= 100
    if dir == "L":
        num = -num
    if (a + num <= 0 and a != 0) or a + num >= 100:
        result += 1
    a = (a + num) % 100
print(result)
