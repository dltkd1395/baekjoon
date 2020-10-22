# 백준[2847]

n=int(input())
s=[int(input()) for _ in range(n)]
c=0

for i in range(n-1, 0, -1):
  if s[i]<=s[i-1]:
    c+=s[i-1]-s[i]+1
    s[i-1]=s[i]-1
print(c)
