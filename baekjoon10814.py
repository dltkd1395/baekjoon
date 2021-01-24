# 백준[10814번]

n=int(input())
data=[]

for i in range(n):
  a,b=input().split()
  data.append([int(a),b])

data.sort(key=lambda x: x[0])

for x in data:
  print(x[0],x[1])
