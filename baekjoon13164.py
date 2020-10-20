# 백준[13164]

n, m = map(int, input().split())

t=list(map(int, input().split()))

cnt=0
for i in range(1, n):
  t[i-1]=t[i]-t[i-1]

t.sort(reverse=False)
for i in range(n-m):
  cnt+=t[i]

print(cnt)
