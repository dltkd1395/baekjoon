# 백준[2667번]

n=int(input())
graph=[]

dx=[-1,0,0,1]
dy=[0,1,-1,0]

def dfs(x,y):
  global building_cnt
  visited[x][y]=1

  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]

    if nx>=0 and nx<n and ny>=0 and ny<n:
      if graph[nx][ny]==1 and visited[nx][ny]==0:
        building_cnt+=1
        dfs(nx,ny)
        
for i in range(n):
  graph.append(list(map(int,input())))

visited=[[0]*n for i in range(n)]

count=0
building=[]
building_cnt=0

for i in range(n):
  for j in range(n):
    if visited[i][j]==0 and graph[i][j]==1:
      building_cnt=1
      dfs(i,j)
      building.append(building_cnt)
      count+=1
print(count)
building.sort()
for i in range(count):
    print(building[i])

