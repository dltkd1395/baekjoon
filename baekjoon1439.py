# 백준[1439]

s=list(input())
cnt=0
for i in range(1, len(s)):
  if s[i]!=s[i-1]:
    cnt+=1
print((cnt+1)//2)
