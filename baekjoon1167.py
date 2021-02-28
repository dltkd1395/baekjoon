# 백준[1167번]

v=int(input())
node_graph=[[] for _ in range(v+1)]
for _ in range(v):
  path=list(map(int,input().split()))

  for i in range(1,len(path)//2):
    node_graph[path[0]].append([path[2*i-1], path[2*i]])

result_first=[0 for _ in range(v+1)]

def DFS(start, matrix, result):
  for x,y in matrix[start]:
    if result[x]==0:
      result[x]=result[start]+y
      DFS(x, matrix, result)

DFS(1, node_graph, result_first)
result_first[1]=0

tmp=0
index=0

for i in range(len(result_first)):
  if result_first[i]>tmp:
    tmp=result_first[i]
    index=i

result_final=[0 for _ in range(v+1)]
DFS(index, node_graph, result_final)
result_final[index]=0
print(max(result_final))

