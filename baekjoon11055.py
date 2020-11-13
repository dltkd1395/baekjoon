# 백준[11055]

n=int(input())

a=list(map(int, input().split()))
dp=[0 for _ in range(n)]

for i in range(n):
  tmp=0
  for j in range(i):
    if a[i]>a[j]:
      tmp=max(tmp,dp[j])
  dp[i]=a[i]+tmp
print(dp)
    
