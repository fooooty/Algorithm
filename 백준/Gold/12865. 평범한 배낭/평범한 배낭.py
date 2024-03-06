import sys
#sys.stdin=open("input.txt","r")
n,m=map(int,sys.stdin.readline().split())
backpack=[[0]*2 for i in range(n)]
dp=[0]*(m+1)
for i in range(n):
  backpack[i][0],backpack[i][1]=map(int,sys.stdin.readline().split())
backpack.sort(key=lambda x:x[0])
for i in range(n):
  for j in range(m,backpack[i][0]-1,-1):
    dp[j]=max(backpack[i][1]+dp[j-backpack[i][0]],dp[j])
print(dp[m])