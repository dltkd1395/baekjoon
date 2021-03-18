# 백준[2447번]


def star(x,y,n):
  if n==1:
    stars[y][x]='*'

  else:
    size=n//3

    for i in range(3):
      for j in range(3):
        if i!=1 or j!=1:
          star(x+i*size, y+j*size, size)
          
n=int(input())
stars=[[' ']*n for _ in range(n)]
star(0,0,n)

for k in stars:
  print(''.join(k))
