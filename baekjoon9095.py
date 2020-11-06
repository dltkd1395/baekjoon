# 백준[9095]

n=int(input())

for i in range(n):
  num=int(input())
  dp=[0, 1, 2, 4]
  if num<=3:
    print(dp[num])
  else:
    for i in range(4,num+1):
      dp.append(sum(dp[-3:]))
    print(dp[-1])
