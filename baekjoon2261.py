# 백준[2261번]

def dis(a,b):
  return (b[0]-a[0])**2+(b[1]-a[1])**2

def solve(start,end):
  leng=end-start
  
  if leng==2:
    return dis(s[start],s[start+1])

  elif leng==3:
    return min(dis(s[start],s[start+1]),dis(s[start+1],s[start+2]))

  leng=(start+end)//2
  mid=s[leng][0]
  d=min(solve(leng,end), solve(start,leng))
  tmp=[]
  for i in range(start,end):
    if (mid-s[i][0])**2 <= d:
      tmp.append(s[i])
  tmp.sort(key=lambda x:x[1])
  m=d
  tmp_len=len(tmp)

  if tmp_len>=2:
    for i in range(tmp_len-1):
      for j in range(i+1,tmp_len):
        if (tmp[i][1]-tmp[j][1])**2 > d:
          break
        elif tmp[i][0] < mid and tmp[j][0] < mid:
          continue
        elif tmp[i][0] > mid and tmp[j][0] > mid:
          continue
        m = min(m, dis(tmp[i],tmp[j]))
  return m

n=int(input())
data=[list(map(int,input().split())) for _ in range(n)]
s=list(set(map(tuple,data)))
if len(s)!=len(data):
  print("0")
else:
  s.sort()
  d=solve(0,len(s))
  print(d)

