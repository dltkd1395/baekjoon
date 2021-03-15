# 백준[11728번]

n,m=map(int,input().split())

n1=list(map(int,input().split()))
m1=list(map(int,input().split()))

lst=n1+m1
lst.sort()

for i in range(len(lst)):
  print(lst[i],end=' ')
