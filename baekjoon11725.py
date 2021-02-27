# 백준[11725번]
import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
head=[0]*(n+1)
head[1]=1
tree={}
for i in range(1,n+1):
  tree[i]=[]

for _ in range(n-1):
  x,y=map(int,input().split())
  tree[x].append(y)
  tree[y].append(x)

q=deque([1])
while q:
  node=q.popleft()

  for child in tree[node]:
    if not head[child]:
      head[child]=node
      q.append(child)

for h in head[2:]:
  print(h)
