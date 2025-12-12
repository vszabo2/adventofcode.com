def num_paths_to_out(graph, start, seen) -> int:
    if start == "out":
        return 1
    return sum(num_paths_to_out(graph, neighbor, seen | frozenset((start,))) for neighbor in graph[start] if neighbor not in seen)


def main() -> None:
    graph = dict[str, list[str]]()
    for line in open("input"):
        a, b = line.split(":")
        graph[a] = b.strip().split()
    print(num_paths_to_out(graph, "you", frozenset(("you",))))

if __name__ == "__main__":
    main()
