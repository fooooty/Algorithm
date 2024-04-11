import sys
from collections import deque
#sys.stdin=open("input.txt")
def checkall(check):
  for i in range(h):
    for j in range(m):
      for k in range(n):
        if check[i][j][k]==0:
          return False
  return True
  
n,m,h=map(int,sys.stdin.readline().split())
maplist=[[[0]*n for _ in range(m) ]for j in range(h)]
queue=deque()
rotten=[[-1,0,0],[1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]
for i in range(h):
  for j in range(m):
    maplist[i][j]=list(map(int,sys.stdin.readline().split()))
    for k in range(n):
      if maplist[i][j][k]==1:
        queue.append([i,j,k])
count=1
checkk=0
while queue:
  x,y,z=queue.popleft()
  count=maplist[x][y][z]
  for i in rotten:
    dx=x+i[0]
    dy=y+i[1]
    dz=z+i[2]
    if 0<=dx<h and 0<=dy<m and 0<=dz<n and maplist[dx][dy][dz]==0:
      queue.append([dx,dy,dz])
      maplist[dx][dy][dz]=count+1
if checkall(maplist)==True:
  print(count-1)
else:
  print(-1)