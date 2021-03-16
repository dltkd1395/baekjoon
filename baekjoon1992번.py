# 백준[1992번]

def check(x,y,n):
  global res

  check_num=data[x][y]

  for i in range(x,x+n):
    for j in range(y,y+n):
      if check_num!=data[i][j]:
        res+="("
        check(x,y,n//2)
        check(x,y+n//2,n//2)
        check(x+n//2,y,n//2)
        check(x+n//2,y+n//2,n//2)
        res+=")"

        return
  
  if check_num==0:
    res+="0"
  else:
    res+="1"


n=int(input())
res=""
data=[list(map(int,input())) for _ in range(n)]
check(0,0,n)
print(res)
