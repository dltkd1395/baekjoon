# 백준[13458]
import math

n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())

cnt=0
for i in range(n):
  b_cnt=a[i]-b
  if b_cnt>0:
    c_cnt=b_cnt/c
    c_cnt=math.ceil(c_cnt)
    cnt+=1+c_cnt
  else:
    cnt+=1
print(cnt)

