import sys
from collections import deque
#sys.stdin=open("input.txt","r")
n,m=map(int,sys.stdin.readline().split())
graph=[]
queue=deque()
ans=10e9
move=[[1,0],[-1,0],[0,1],[0,-1]]
for i in range(n):
  empty=str(sys.stdin.readline().rstrip())
  graph.append(list(map(int,list(empty))))

check=[[[0]*m for i in range(n)] for j in range(2)]
check[0][0][0]=1
queue.append((0,0,0))
while queue:
  x,y,z=queue.popleft()
  if x==n-1 and y==m-1:
    print(check[z][x][y])
    exit()
  for i in move:
    nx=x+i[0]
    ny=y+i[1]
    if nx>=0 and nx<n and ny>=0 and ny<m:
      if z==0:
        if graph[nx][ny]==0 and check[0][nx][ny]==0:
          check[0][nx][ny]=check[0][x][y]+1
          queue.append((nx,ny,0))
        elif graph[nx][ny]==1 and check[1][nx][ny]==0:
          check[1][nx][ny]=check[0][x][y]+1
          queue.append((nx,ny,1))
      else:
        if graph[nx][ny]==0 and check[1][nx][ny]==0:
          check[1][nx][ny]=check[1][x][y]+1
          queue.append((nx,ny,1))
print(-1)