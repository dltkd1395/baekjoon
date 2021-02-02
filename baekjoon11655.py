# 백준[11655번]

n=list(input())
capital='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower='abcdefghijklmnopqrstuvwxyz'
data=[]
for x in n:
  if ord(x)>=65 and ord(x)<=90:
    a=capital[ord(x)%26]
    data.append(a)
  elif ord(x)>=97 and ord(x)<=122:
    b=lower[(ord(x)-32)%26]
    data.append(b)
  else:
    data.append(x)

for i in range(len(data)):
  print(data[i],end='')
