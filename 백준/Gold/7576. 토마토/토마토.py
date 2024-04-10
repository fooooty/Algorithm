import sys
from collections import deque
#sys.stdin=open("input.txt")
def checkall(check):
  for i in check:
    if 0 in i:
      return False
  return True
n,m=map(int,sys.stdin.readline().split())
maplist=[]
queue=deque()
rotten=[[-1,0],[1,0],[0,1],[0,-1]]
for i in range(m):
  maplist.append(list(map(int,sys.stdin.readline().split())))
  for j in range(n):
    if maplist[i][j]==1:
      queue.append([i,j])
count=1
checkk=0
while queue:
  x,y=queue.popleft()
  count=maplist[x][y]
  for i in rotten:
    dx=x+i[0]
    dy=y+i[1]
    if 0<=dx<m and 0<=dy<n and maplist[dx][dy]==0:
      queue.append([dx,dy])
      maplist[dx][dy]=count+1
if checkall(maplist)==True:
  print(count-1)
else:
  print(-1)