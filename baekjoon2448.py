# 백준[2448번]

def stars(x,y,n):

  if n==3:
    star[x][y]='*'
    star[x+1][y-1]='*'
    star[x+1][y+1]='*'
    star[x+2][y]='*'
    star[x+2][y-1]='*'
    star[x+2][y-2]='*'
    star[x+2][y+1]='*'
    star[x+2][y+2]='*'

  else:
    size=n//2
    stars(x,y,size)
    stars(x+size,y-size,size)
    stars(x+size,y+size,size)

n=int(input())
star=[[' ']*(n*2) for _ in range(n)]
stars(0,n-1,n)

for k in star:
  print(''.join(k))

