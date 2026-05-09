# Task5_BFS.py

from collections import deque

with open("input5.txt") as f:
    n, m = map(int, f.readline().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, f.readline().split())
        graph[u].append(v)
        graph[v].append(u)

visited = [False] * (n + 1)
q = deque([1])
visited[1] = True
order = []

while q:
    node = q.popleft()
    order.append(node)

    for nxt in graph[node]:
        if not visited[nxt]:
            visited[nxt] = True
            q.append(nxt)

with open("output5.txt", "w") as f:
    f.write(" ".join(map(str, order)))