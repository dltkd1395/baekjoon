#백준[14720]

n=int(input())
m=list(map(int, input().split()))
c=0
for i in range(n):
  if m[i]==c%3:
    c+=1

print(c)
