# 백준[11652번]

n = int(input())
dic = {}

for _ in range(n):
    idex = int(input())
    if idex in dic:
        dic[idex] += 1
    else:
        dic[idex] = 1

dic = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
print(dic[0][0])
