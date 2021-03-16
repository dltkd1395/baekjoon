# 백준[1780번]

n=int(input())

data=[list(map(int,input().split())) for _ in range(n)]

num=0
num0=0
num1=0

def split_num(x,y,n):
  global num, num0, num1

  num_check=data[x][y]

  for i in range(x,x+n):
    for j in range(y,y+n):
      if num_check!=data[i][j]:
        for k in range(3):
          for l in range(3):
            split_num(x+k*n//3, y+l*n//3, n//3)
        
        return
  
  if num_check==-1:
    num+=1
  
  if num_check==0:
    num0+=1
  
  if num_check==1:
    num1+=1

split_num(0,0,n)
print(num)
print(num0)
print(num1)

