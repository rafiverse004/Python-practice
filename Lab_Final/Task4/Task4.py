# Task4.py

with open("input4.txt") as f:
    n, m = map(int, f.readline().split())
    graph = [[0] * (n + 1) for _ in range(n + 1)]

    for _ in range(m):
        u, v, w = map(int, f.readline().split())
        graph[u][v] = w

with open("output4.txt", "w") as f:
    for i in range(n + 1):
        f.write(" ".join(map(str, graph[i])) + "\n")