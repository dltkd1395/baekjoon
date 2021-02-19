# 백준[10451번]

import sys
sys.setrecursionlimit(2000)

def dfs(x):
  visited[x]=1
  number=num[x]

  if visited[number]==0:
    dfs(number)

t=int(input())

for i in range(t):
  n=int(input())
  num=[0]+list(map(int,input().split()))
  visited=[1]+[0]*n
  count=0

  for i in range(1,n+1):
    if visited[i]==0:
      dfs(i)
      count+=1

  print(count)
