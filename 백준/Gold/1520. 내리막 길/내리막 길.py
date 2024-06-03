import sys 
def dfs(x,y,graph):
  global dp,n,m
  if x==n and y==m:
    dp[x][y]=1
    return 1
  dp[x][y]=0
  if x-1>=1 and graph[x-1][y]<graph[x][y]:
    if dp[x-1][y]!=-1:
      dp[x][y]+=dp[x-1][y]
    else:
      dp[x][y]+=dfs(x-1,y,graph)
  if x+1<=n and graph[x+1][y]<graph[x][y]:
    if dp[x+1][y]!=-1:
      dp[x][y]+=dp[x+1][y]
    else:
      dp[x][y]+=dfs(x+1,y,graph)
  if y-1>=1 and graph[x][y-1]<graph[x][y]:
    if dp[x][y-1]!=-1:
      dp[x][y]+=dp[x][y-1]
    else:
      dp[x][y]+=dfs(x,y-1,graph)
  if y+1<=m and graph[x][y+1]<graph[x][y]:
    if dp[x][y+1]!=-1:
      dp[x][y]+=dp[x][y+1]
    else:
      dp[x][y]+=dfs(x,y+1,graph)
  return dp[x][y]
    
#sys.stdin=open("input.txt","r")
n,m=map(int,sys.stdin.readline().split())
graph=[[0]]
dp=[[-1]*(m+1) for i in range(n+1)]
for i in range(n):
  graph.append([0]+list(map(int,sys.stdin.readline().split())))
dp[1][1]=dfs(1,1,graph)
print(dp[1][1])