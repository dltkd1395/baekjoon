# 백준[11576번]

A,B=map(int,input().split())
m=int(input())
num=list(map(int,input().split()))
n=0
res=[]
for i in range(len(num)):
  n=n+(num.pop()*(A**i))

while n:
  res.append(n%B)
  n//=B

for _ in range(len(res)):
  print(res.pop(), end=' ')
