import sys
#sys.stdin=open("input.txt","r")
n,m=map(int,sys.stdin.readline().split())
ans=[[10e9]*(n+1) for i in range(n+1)]
for i in range(m):
  a,b,c=map(int,sys.stdin.readline().split())
  ans[a][b]=min(ans[a][b],c)
for i in range(1,n+1):
  for j in range(1,n+1):
    for k in range(1,n+1):
      if j==k:
        ans[j][k]=0
      elif ans[j][i]!=10e9 and ans[i][k]!=10e9:
        ans[j][k]=min(ans[j][k],ans[j][i]+ans[i][k])
realans=10e9
for i in range(1,n):
  for j in range(i+1,n+1):
    if ans[i][j]!=10e9 and ans[j][i]!=10e9:
      realans=min(realans,ans[i][j]+ans[j][i])
if realans!=10e9:
  print(realans)
else:
  print(-1)