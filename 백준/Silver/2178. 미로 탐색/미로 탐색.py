import sys
#sys.stdin=open("input.txt","r")
sys.setrecursionlimit(10**5)
def bfs(x,y):
  global n,m,queue,check,miro,ans
  if x==n-1 and y==m-1:
    return
  check[x][y]=1
  queue.pop(0)
  if x-1>=0 and miro[x-1][y]=='1' and check[x-1][y]==0:
    queue.append((x-1,y))
    ans[x-1][y]=ans[x][y]+1
    check[x-1][y]=1
  if x+1<n and miro[x+1][y]=='1' and check[x+1][y]==0:
    queue.append((x+1,y))
    ans[x+1][y]=ans[x][y]+1
    check[x+1][y]=1
  if y-1>=0 and miro[x][y-1]=='1' and check[x][y-1]==0:
    queue.append((x,y-1))
    ans[x][y-1]=ans[x][y]+1
    check[x][y-1]=1
  if y+1<m and miro[x][y+1]=='1' and check[x][y+1]==0:
    queue.append((x,y+1))
    ans[x][y+1]=ans[x][y]+1
    check[x][y+1]=1
  if queue:
    bfs(queue[0][0],queue[0][1])

miro=[]
queue=[]
n,m=map(int,sys.stdin.readline().split())
check=[[0]*m for i in range(n)]
ans=[[0]*m for i in range(n)]
for i in range(n):
  miro.append(list(sys.stdin.readline().rstrip()))
queue.append((0,0))
bfs(0,0)
print(ans[n-1][m-1]+1)