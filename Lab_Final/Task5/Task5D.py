# Task5_DFS.py
import sys
sys.setrecursionlimit(10**6)

with open("input5.txt") as f:
    n, m = map(int, f.readline().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, f.readline().split())
        graph[u].append(v)
        graph[v].append(u)

visited = [False] * (n + 1)
order = []

def dfs(node):
    visited[node] = True
    order.append(node)
    for nxt in graph[node]:
        if not visited[nxt]:
            dfs(nxt)

dfs(1)

with open("output5.txt", "w") as f:
    f.write(" ".join(map(str, order)))