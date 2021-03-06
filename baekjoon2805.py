# 백준[2805번]

n,m=map(int,input().split())
array=list(map(int,input().split()))

start,end=0,max(array)
ans=0

def sum(height):
  sum=0

  for i in array:
    if i-height>0:
      sum+=i-height

  return sum

while start<=end:
  mid=(start+end)//2
  len=0

  len=sum(mid)

  if len>=m:
    ans=mid
    start=mid+1
  else:
    end=mid-1
print(ans)
