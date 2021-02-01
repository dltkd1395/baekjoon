# 백준[10809번]

strings=list(input())

data=[-1]*26
count=0

for x in strings:
  index=26-(122%ord(x))-1
  if data[index]==-1:
    data[index]=count
    count+=1
  else:
    count+=1

for i in range(26):
  print(data[i],end=' ')
