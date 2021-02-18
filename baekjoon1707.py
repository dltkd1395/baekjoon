# 백준[1707번]
from collections import deque

k=int(input())

def bfs(start):
  visited[start]=1
  q=deque()
  q.append(start)
  while q:
    a=q.popleft()
    for i in graph[a]:
      if visited[i]==0:
        visited[i]=-visited[a]
        q.append(i)
      else:
        if visited[i]==visited[a]:
          return False
  return True


for i in range(k):
  v,e=map(int,input().split())
  graph=[[] for i in range(v+1)]
  visited=[0 for i in range(v+1)]
  isTrue=True
  for j in range(e):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
  
  for k in range(1,v+1):
    if visited[k]==0:
      if not bfs(k):
        isTrue=False
        break
  print('YES' if isTrue else 'NO')

    
