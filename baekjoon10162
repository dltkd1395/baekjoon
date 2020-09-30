# 백준[10162]

time = int(input())
cnt = [0]*3
time_arr=[300, 60, 10]

for i in range(len(time_arr)):
  if time >= time_arr[i]:
    count=time//time_arr[i]
    time-=time_arr[i]*count
    cnt[i] = count
    
if time == 0:
  for i in range(len(cnt)):
    print(cnt[i], end=' ')
else:
  print('-1')
