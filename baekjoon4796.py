# 백준[4796]
i=1
while True:
  L, P, V = map(int, input().split())
  if L==0 and P==0 and V==0:
    break

  result = (V//P)*L
  result+=min((V%P),L)
  print('Case %d: %d' %(i,result))
  i+=1

