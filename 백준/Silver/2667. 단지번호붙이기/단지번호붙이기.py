import sys
#sys.stdin=open("input.txt","r")
sys.setrecursionlimit(10**5)
def dfs(home,x,y):
  global check,n,homecount
  homecount+=1
  check[x][y]=1
  if y-1>=0:
    if check[x][y-1]==0 and home[x][y-1]=='1':
      dfs(home,x,y-1)
  if x-1>=0:
    if check[x-1][y]==0 and home[x-1][y]=='1':
      dfs(home,x-1,y)
  if y+1<n:
    if check[x][y+1]==0 and home[x][y+1]=='1':
      dfs(home,x,y+1)
  if x+1<n:
    if check[x+1][y]==0 and home[x+1][y]=='1':
      dfs(home,x+1,y)
      
home=[]
ans=0
anslist=[]
n=int(sys.stdin.readline())
check=[[0]*(n) for i in range(n)]
for i in range(n):
  home.append(list(sys.stdin.readline().rstrip()))
for i in range(n):
  for j in range(n):
    if home[i][j]=='1' and check[i][j]==0:
      ans+=1
      homecount=0
      dfs(home,i,j)
      anslist.append(homecount)
print(ans)
anslist.sort()
for i in anslist:
  print(i)