# 백준[10808번]

string=list(input())

data=[0]*26

for x in string:
  index=26-(122%ord(x))-1
  data[index]+=1

for i in range(26):
  print(data[i],end=' ')
