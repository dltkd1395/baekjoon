# 백준[11047]

num, money = input().split()
num, money = int(num), int(money)
count=0
ch_money=[]
for i in range(num):
  won=int(input())
  ch_money.append(won)
ch_money.reverse()

for i in range(num):
  if money>=ch_money[i]:
    coin=money//ch_money[i]
    money-=ch_money[i]*coin
    count+=coin
print(count)