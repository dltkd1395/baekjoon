# 백준[9461]

n=int(input())
dp=[1]*101
num=[int(input()) for _ in range(n)]

for i in range(3,101):
  dp[i]=dp[i-3]+dp[i-2]

for i in range(n):
  print(dp[num[i]-1])
