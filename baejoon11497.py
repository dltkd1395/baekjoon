# 백준[11497]

n=int(input())

for _ in range(n):
  num=int(input())
  h=list(map(int, input().split()))
  h.sort()
  ans=0
  for i in range(2,num):
    c=abs(h[i]-h[i-2])
    ans=max(c, ans)
  print(ans)
