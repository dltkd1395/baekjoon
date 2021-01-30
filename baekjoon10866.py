# 백준[10866번]
from collections import deque

n=int(input())
data=deque([])
for i in range(n):
  a=list(input().split())

  if a[0]=='push_front':
    data.appendleft(a[1])
  elif a[0]=='push_back':
    data.append(a[1])
  elif a[0]=='pop_front':
    if len(data)==0:
      print('-1')
    else:
      print(data.popleft())
  elif a[0]=='pop_back':
    if len(data)==0:
      print('-1')
    else:
      print(data.pop())
  elif a[0]=='size':
    print(len(data))
  elif a[0]=='empty':
    if len(data)==0:
      print('1')
    else:
      print('0')
  elif a[0]=='front':
    if len(data)==0:
      print('-1')
    else:
      print(data[0])
  elif a[0]=='back':
    if len(data)==0:
      print('-1')
    else:
      print(data[-1])
