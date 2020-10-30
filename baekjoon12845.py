# 백준[12845]

n=int(input())
L=list(map(int, input().split()))
m=L.index(max(L))
r=L.pop(m)
cnt=0
for i in range(len(L)):
  cnt+=L[i]+r

print(cnt)
