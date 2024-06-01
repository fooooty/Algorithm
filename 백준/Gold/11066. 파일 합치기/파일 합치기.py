import sys

#sys.stdin=open("input.txt","r")
k=int(sys.stdin.readline())
for i in range(k):
  n=int(sys.stdin.readline())
  ans=[[10e9]*(n+1) for j in range(n+1)]
  graph=[0]+list(map(int,sys.stdin.readline().split()))
  sum=[0]*(n+1)
  ans[1][1]=0
  ans[1][2]=graph[1]+graph[2]
  ans[2][2]=0
  for j in range(1,n+1):
    sum[j]=sum[j-1]+graph[j]
  for j in range(3,n+1):
    for k in range(j,0,-1):
      if j==k:
        ans[j][k]=0
      else:
        for l in range(k,j):
          cnt=ans[k][l]+ans[l+1][j]+sum[j]-sum[k-1]
          ans[k][j]=min(ans[k][j],cnt)
  print(ans[1][n])