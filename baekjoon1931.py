# 백준[1931]

num = int(input())
s=[]
for i in range(num):
    schedule = list(map(int, input().split()))
    s.append(schedule)
s=sorted(s, key = lambda a:a[0])
s=sorted(s, key = lambda a:a[1])

last=0
count = 0
for i, j in s:
    if i>=last:
        count+=1
        last=j

print(count)