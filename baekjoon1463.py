# 백준[1463]

n=int(input())
dp_lst=[0,0,1,1]

for i in range(4,n+1):
  dp_lst.append(dp_lst[i-1]+1)
  
  if i%2==0:
    dp_lst[i]=min(dp_lst[i],dp_lst[i//2]+1)
  if i%3==0:
    dp_lst[i]=min(dp_lst[i],dp_lst[i//3]+1)

print(dp_lst[-1])
