# 백준[2331번]

def next(a,p):
  A=str(a)
  value=0
  for i in A:
    value+=int(i)**p
  return value

def dfs(a,p,count,check):
  if check[a]!=0:
    return check[a]-1
  check[a]=count
  b=next(a,p)
  count+=1
  return dfs(b,p,count,check)



a,p=map(int,input().split())
check=[0]*250000
count=1
print(dfs(a,p,count,check))

