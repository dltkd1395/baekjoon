# 백준[11726]
n=int(input())

dp=[0, 1, 2, 3]

if n<=3:
  print(n)
else:
  for i in range(3, n+1):
    dp[i]=dp[i-1]+dp[i-2]
    dp.append(dp[i])
  print(dp[i]%10007)
