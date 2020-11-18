# 백준[1912]

n=int(input())

a=list(map(int,input().split()))
dp=[0 for _ in range(n)]

for i in range(n):
  tmp=0
  for j in range(i):
    if a[i]>a[j]:
      dp[i]=a[i]+a[j]
  dp[i]=tmp
print(dp)

