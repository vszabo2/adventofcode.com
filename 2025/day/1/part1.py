result = 0
a = 50
for line in open("input.txt"):
    dir = line[0]
    num = int(line[1:])
    if dir == "L":
        num = -num
    a += num
    a %= 100
    if a == 0:
        result += 1
print(result)
