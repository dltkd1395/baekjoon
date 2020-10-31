# 백준[14916]

n=int(input())
o=n%5
if n==1 or n==3:
  cnt=-1
elif o%2==0:
  cnt=n//5+o//2
else:
  cnt=((n//5)-1)+((o+5)//2)

print(cnt)
