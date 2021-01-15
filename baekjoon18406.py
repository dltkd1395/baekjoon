# 백준[18406번]

n=list(map(int,input()))
num=len(n)
if num%2==1:
  exit()

elif num%2==0:
  a=num//2
  left=0
  right=0
  for i in range(a):
    left+=n[i]
  
  for i in range(a,num):
    right+=n[i]

  if left==right:
    print('LUCKY')
  else:
    print('READY')

'''
n=input()
length=len(n)
summary=0

for i in range(length//2):
  summary+=int(n[i])

for i in range(length//2,length):
  summary-=int(n[i])

if summary==0:
  print("LUCKY")
else:
  print("READY")
'''
