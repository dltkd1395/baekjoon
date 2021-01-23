# 백준[11651번]

n=int(input())
data=[]
for i in range(n):
  data.append(list(map(int,input().split())))

data.sort(key=lambda x: (x[1],x[0]))

for x in data:
  print(x[0],x[1])
