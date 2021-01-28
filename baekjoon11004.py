# 백준[11004번]

n,k=map(int,input().split())

data=list(map(int,input().split()))
data=sorted(data,reverse=False)

print(data[k-1])
