# inspired by reddit
f = lambda a, b: (int(a) // 3) * (int(b) // 3)
g = lambda a, b: f(*a.split("x")) >= sum(map(int, b.split()))
print(sum(g(*i.split(":")) for i in open("input").read().strip().split("\n\n")[-1].split("\n")))
