import sys
#sys.stdin=open("input.txt","r")
abc=' '+str(sys.stdin.readline().rstrip())
abc=list(abc)
n=int(sys.stdin.readline())
dp=[[0]*(len(abc)) for i in range(27)]
dp[ord(abc[1])-96][1]=1
for i in range(2,len(abc)):
  for j in range(1,27):
    if ord(abc[i])-96==j:
      dp[j][i]=dp[j][i-1]+1
    else:
      dp[j][i]=dp[j][i-1]
#print(dp)
for i in range(n):
  m=list(sys.stdin.readline().rstrip().split())
  m[0]=ord(m[0])-96
  m[1]=int(m[1])
  m[2]=int(m[2])
  print(dp[m[0]][m[2]+1]-dp[m[0]][m[1]])