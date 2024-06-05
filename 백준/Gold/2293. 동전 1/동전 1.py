import sys
#sys.stdin=open("input.txt","r")
n,m=map(int,sys.stdin.readline().split())
dp=[0]*(m+1)
graph=[]
for i in range(n):
  graph.append(int(sys.stdin.readline()))
graph.sort()
dp[0]=1
for i in range(n):
  for j in range(0,m+1):
    if dp[j]!=0 and graph[i]+j<=m:
      dp[graph[i]+j]+=dp[j]
print(dp[m])