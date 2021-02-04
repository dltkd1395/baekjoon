# 백준[1406번]

s1=list(input())
s2=[]
n=int(input())

for i in range(n):
  s=input().split()
  if s[0]=='P':
    s1.append(s[1])
  elif s[0]=='L' and s1!=[]:
    s2.append(s1.pop())
  elif s[0]=='D' and s1!=[]:
    s1.append(s2.pop())
  elif s[0]=='B' and s1!=[]:
    s1.pop()

print(''.join(s1+list(reversed(s2))))
