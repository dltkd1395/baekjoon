# 백준[1158번]

n,k=map(int,input().split())

data=[i for i in range(1,n+1)]
answer=[]
num=0

for i in range(n):
  num+=k-1
  if num>=len(data):
    num=num%len(data)
  answer.append(str(data.pop(num)))

print('<'+', '.join(answer[:])+'>',sep='')
