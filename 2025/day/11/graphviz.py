print("digraph {")
for line in open("input"):
    a, b = line.split(":")
    for c in b.strip().split():
        print(f"{a} -> {c}")
print("}")
