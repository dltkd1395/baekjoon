# 백준[11000]

from queue import PriorityQueue
import sys
s=sys.stdin.readline
def main():
  n = int(s())
  num = []
  pque = PriorityQueue()
  for i in range(n):
      num.append(list(map(int,s().split())))
  num = sorted(num,key = lambda x: (x[0],x[1]))

  for i in range(n):
      if pque.qsize() != 0 and pque.queue[0][1]<= num[i][0]:
          pque.get()
      pque.put((num[i][1],num[i][1]))
  print(pque.qsize())

if __name__ == '__main__':
  main()
