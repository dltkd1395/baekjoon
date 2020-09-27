# 백준[11399]
a=int(input())
b=list(map(int, input().split()))
b.sort()
c=0
for i in range(a):
    for j in range(a-1-i,-1,-1):
        c+=b[j]
print(c)
