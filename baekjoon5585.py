# 백준[5585]

a = int(input())
b = 1000 - a
c = [500, 100, 50, 10, 5, 1]
count = 0
for i in range(6):
    coin = c[i]
    if b >= c[i]:
        mok = b // coin
        b -= coin * mok
        count += mok

print(count)