# 백준[1138]

num=int(input())
line_lst = [0 for _ in range(num)]
line=list(map(int, input().split()))
for i in range(1, num+1):
  cnt=0
  a=line[i-1]
  for j in range(num):
    if cnt==a:
      if line_lst[j]==0:
        line_lst[j]=i
        break
    elif line_lst[j]==0:
      cnt+=1

for i in range(len(line_lst)):
  print(line_lst[i], end=' ')

  
