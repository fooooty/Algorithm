import sys
#sys.stdin=open("input.txt","r")
sys.setrecursionlimit(10**5)
def dfs(home,xx,yy):
  global check,x,y
  check[xx][yy]=1
  if yy-1>=0:
    if check[xx][yy-1]==0 and home[xx][yy-1]=='1':
      dfs(home,xx,yy-1)
  if xx-1>=0:
    if check[xx-1][yy]==0 and home[xx-1][yy]=='1':
      dfs(home,xx-1,yy)
  if yy+1<y:
    if check[xx][yy+1]==0 and home[xx][yy+1]=='1':
      dfs(home,xx,yy+1)
  if xx+1<x:
    if check[xx+1][yy]==0 and home[xx+1][yy]=='1':
      dfs(home,xx+1,yy)


n=int(sys.stdin.readline())
for i in range(n):
  ans=0
  x,y,k=map(int,sys.stdin.readline().split())
  home=[['0']*y for _ in range(x)]
  check=[[0]*y for _ in range(x)]
  for j in range(k):
    a,b=map(int,sys.stdin.readline().split())
    home[a][b]='1'
  for j in range(x):
    for l in range(y):
      if home[j][l]=='1' and check[j][l]==0:
        ans+=1
        dfs(home,j,l)
  print(ans)