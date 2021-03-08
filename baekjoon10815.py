 # 백준[10815번]

def binary_search(array,target,start,end):
  if start>end:
    return 0

  mid=(start+end)//2

  if array[mid]==target:
    return 1

  elif array[mid]>=target:
    return binary_search(array,target,start,mid-1)
  else:
    return binary_search(array,target,mid+1,end)


n=int(input())
num=list(map(int,input().split()))
m=int(input())
array=list(map(int,input().split()))

num.sort()
data=[]
for i in range(m):
  res=binary_search(num,array[i],0,len(num)-1)
  data.append(res)

for i in range(m):
  print(data[i],end=' ')
