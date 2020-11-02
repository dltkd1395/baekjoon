# 백준[15904]

strings=input()
compare=['U','C','P','C']
check=True

for i in range(len(compare)):
  if compare[i] in strings:
    check=True
    idx=strings.find(compare[i])
    strings=strings[idx+1:]
  else:
    check=False
    break
if check==True:
  print('I love UCPC')
else:
  print('I hate UCPC')
