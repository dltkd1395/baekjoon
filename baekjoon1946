#백준[1946]
import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
  n=int(input())
  cv=[list(map(int, input().split())) for _ in range(n)]
  cv.sort()
  interview = [cv[i][1] for i in range(n)]
  res = 1
  grade = interview[0]
  for i in range(1, n):
    grade = min(grade, interview[i])
    if grade == interview[i]:
      res += 1
  print(res)
