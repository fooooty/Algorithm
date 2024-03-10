import sys
#sys.stdin=open("input.txt","r")
m,n,k=map(int,sys.stdin.readline().rstrip().split())
bw=[]
check1=[[0]*n for i in range(m)]
check2=[[1]*n for i in range(m)]
for i in range(m):
  bw.append(list(str(sys.stdin.readline().rstrip())))
  for j in range(n):
    if bw[i][j]=='B':
      bw[i][j]=1
    else:
      bw[i][j]=0
  if i%2==0:
    for j in range(0,n,2):
      check1[i][j]=1
      check2[i][j]=0
  else:
    for j in range(1,n,2):
      check1[i][j]=1
      check2[i][j]=0
dp1=[[0]*(n+1) for i in range(m+1)]
dp2=[[0]*(n+1) for i in range(m+1)]
for i in range(1,m+1):
  for j in range(1,n+1):
    if check1[i-1][j-1]!=bw[i-1][j-1]:
      dp1[i][j]=1
    dp1[i][j]+=dp1[i][j-1]+dp1[i-1][j]-dp1[i-1][j-1]
    if check2[i-1][j-1]!=bw[i-1][j-1]:
      dp2[i][j]=1
    dp2[i][j]+=dp2[i][j-1]+dp2[i-1][j]-dp2[i-1][j-1]
ans=10e9
for i in range(1,m+1):
  if i+k-1<=m:
    for j in range(1,n+1):
      sum1=0
      sum2=0
      if j+k-1<=n:
        sum1+=dp1[i+k-1][j+k-1]-dp1[i+k-1][j-1]-dp1[i-1][j+k-1]+dp1[i-1][j-1]
        sum2+=dp2[i+k-1][j+k-1]-dp2[i+k-1][j-1]-dp2[i-1][j+k-1]+dp2[i-1][j-1]
        ans=min(ans,min(sum2,sum1))
print(ans)