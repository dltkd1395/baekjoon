# 백준[14659]

n=int(input())
h=list(map(int, input().split()))
max_h=0
cnt=0
ans=0
for hill in h:
  if hill > max_h:
    max_h=hill
    cnt=0
  else:
    cnt+=1
  ans=max(ans ,cnt)
print(ans)
