# 백준[11724번]
import sys
sys.setrecursionlimit(10000)
input=sys.stdin.readline

n, m = map(int, input().split())
graph = [[0] * (n + 1) for i in range(n + 1)]
visited = [0 for i in range(n + 1)]
count = 0
def dfs(i):
    visited[i] = 1
    for k in range(1, n + 1):
        if graph[i][k] == 1 and visited[k] == 0:
            dfs(k)
for i in range(m):
    a, b = map(int, input().split())
    s[a][b] = 1
    s[b][a] = 1
for i in range(1, n + 1):
    if visited[i] == 0:
        dfs(i)
        count += 1
print(count)
