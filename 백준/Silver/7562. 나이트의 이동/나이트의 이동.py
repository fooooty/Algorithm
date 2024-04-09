import sys
from collections import deque
#sys.stdin=open("input.txt")
n=int(sys.stdin.readline())
knight=[[-1,-2],[-2,-1],[-2,1],[-1,2],[1,-2],[2,-1],[1,2],[2,1]]
for i in range(n):
  queue=deque()
  m=int(sys.stdin.readline())
  check=[[0]*m for i in range(m)]
  ax,ay=map(int,sys.stdin.readline().split())
  bx,by=map(int,sys.stdin.readline().split())
  count=1
  queue.append([ax,ay])
  breakpoint=0
  while queue:
    x,y=queue.popleft()
    if x==bx and y==by:
      print(0)
      break
    count=check[x][y]
    for i in knight:
      nx=x+i[0]
      ny=y+i[1]
      if 0<=nx<m and 0<=ny<m and check[nx][ny]==0:
        queue.append([nx,ny])
        check[nx][ny]=count+1
        if nx==bx and ny==by:
          print(check[nx][ny])
          breakpoint=1
          break
    if breakpoint==1:
      break
  