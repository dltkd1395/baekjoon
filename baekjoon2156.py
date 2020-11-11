# 백준[2156]

n=int(input())
table=[0]
for _ in range(n):
  table.append(int(input()))

dp=[0]
dp.append(table[1])
if n>1:
  dp.append(table[1]+table[2])
  for i in range(3,n+1):
    dp.append(max(dp[i-3]+table[i-1]+table[i], dp[i-2]+table[i], dp[i-1]))
print(dp[n])
