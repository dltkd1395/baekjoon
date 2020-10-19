# 백준[11508]

n=int(input())
m=[int(input()) for i in range(n)]
c=0
m.sort(reverse=True)
for i in range(n):
  if(i%3!=2):
    c += m[i]
print(c)
