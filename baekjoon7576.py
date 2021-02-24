# 백준[7576번]
from collections import deque

dx=[1,0,0,-1]
dy=[0,-1,1,0]
q=deque()
def bfs():
 
  while q:
    x,y=q.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]

      if nx>=0 and nx<n and ny>=0 and ny<m and graph[nx][ny]==0:
        graph[nx][ny]=graph[x][y]+1
        q.append((nx,ny))


m,n=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]

for i in range(n):
  for j in range(m):
    if graph[i][j]==1:
      q.append((i,j))
bfs()
isTrue=False
result=-2

for i in graph:
  for j in i:
    if j==0:
      isTrue=True
    result=max(result,j)

if isTrue==True:
  print(-1)
elif result==-1:
  print(0)
else:
  print(result-1)
