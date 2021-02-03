# 백준[11656번]

strings=list(input())

data=[]
while len(strings)>0:
  data.append(''.join(strings))
  strings.pop(0)

data.sort()

for i in range(len(data)):
  print(data[i])
