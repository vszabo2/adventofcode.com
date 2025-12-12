from functools import cache

graph = dict[str, list[str]]()


@cache
def num_paths(start, end) -> int:
    if start == end:
        return 1
    if start not in graph:
        return 0
    return sum(num_paths(neighbor, end) for neighbor in graph[start])


def main() -> None:
    for line in open("input"):
        a, b = line.split(":")
        graph[a] = b.strip().split()
    print(
        num_paths("svr", "fft") * num_paths("fft", "dac") * num_paths("dac", "out") 
        + num_paths("svr", "dac") * num_paths("dac", "fft") * num_paths("fft", "out"))

if __name__ == "__main__":
    main()
