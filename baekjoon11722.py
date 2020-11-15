# 백준[11722]

n=int(input())
a=list(map(int, input().split()))

dp=[1 for _ in range(n)]

for i in range(n):
  for j in range(i):
    if a[i]<a[j]:
      dp[i]=max(dp[j]+1, dp[i])
      
  
print(dp)
