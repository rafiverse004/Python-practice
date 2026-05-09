# Task6.py
from collections import deque

with open("input6.txt") as f:
    n, m, d = map(int, f.readline().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, f.readline().split())
        graph[u].append(v)
        graph[v].append(u)

visited = [False] * (n + 1)
parent = [0] * (n + 1)
dist = [0] * (n + 1)

q = deque([1])
visited[1] = True

while q:
    node = q.popleft()
    for nxt in graph[node]:
        if not visited[nxt]:
            visited[nxt] = True
            parent[nxt] = node
            dist[nxt] = dist[node] + 1
            q.append(nxt)

# path reconstruction
path = []
cur = d
while cur != 0:
    path.append(cur)
    cur = parent[cur]
path.reverse()

with open("output6.txt", "w") as f:
    f.write(f"Time: {dist[d]}\n")
    f.write("Shortest Path: " + " ".join(map(str, path)))