import sys

#sys.stdin=open("input.txt","r")
n=int(sys.stdin.readline())
dp=[[10e9]*(n+1) for i in range(n+1)]
graph=[[0]]
for i in range(n):
  graph.append(list(map(int,sys.stdin.readline().split())))
for i in range(1,n+1):
  for j in range(i,0,-1):
    if i==j:
      dp[i][j]=0
    for l in range(j,i):
      empty=dp[j][l]+dp[l+1][i]+graph[j][0]*graph[l][1]*graph[i][1]
      dp[j][i]=min(dp[j][i],empty)
print(dp[1][n])
    