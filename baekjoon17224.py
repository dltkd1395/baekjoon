# 백준[17224]

n, l, k=map(int,input().split())

c=0
num=0
lst=[]
for i in range(n):
  number=list(map(int,input().split()))
  lst.append(number)

for i in range(n):
    if lst[i][1]<=l and num<k:
      c+=140
      num+=1
      
for i in range(n):
  if lst[i][0]<=l and lst[i][1]>l and num < k: 
    c+=100
    num+=1
print(c)
