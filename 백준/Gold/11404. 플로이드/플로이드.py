import sys
#sys.stdin=open("input.txt","r")
n=int(sys.stdin.readline())
m=int(sys.stdin.readline())
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
for i in range(1,n+1):
  for j in range(1,n+1):
    if ans[i][j]!=10e9:
      print(ans[i][j],end=" ")
    else:
      print(0,end=" ")
  print('')