# 백준[10828번]

n=int(input())
data=[]
for i in range(n):
  a=list(input().split())

  if a[0]=='push':
    data.append(a[1])
  elif a[0]=='pop':
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
  elif a[0]=='top':
    if len(data)==0:
      print('-1')
    else:
      print(data[-1])


