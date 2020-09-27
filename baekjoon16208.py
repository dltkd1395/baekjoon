# 백준[16208]

a=int(input())
b=list(map(int, input().split()))
c=[]
count=0
if a>=1 and a<=5000:
  for i in range(a):
    for j in range(i+1,a):
      c.append(b[i]*b[j])

  for i in range(len(c)):
    count += c[i]
  print(count)
