import sys
#sys.stdin=open("input.txt","r")
n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline())
b=list(map(int,sys.stdin.readline().split()))
cnt=0
for i in a:
  cnt+=i
dp=[0]*(cnt+1)
dp[0]=-1
for i in range(n):
  for j in range(0,cnt+1):
    if dp[j]!=0 and dp[j]!=i+1:
      if dp[abs(j-a[i])]==0:
        dp[abs(j-a[i])]=(i+1)
      if j+a[i]<=cnt and dp[j+a[i]]==0:
        dp[j+a[i]]=(i+1)
for j in b:
  if j>=cnt+1:
    print('N',end=' ')
  elif dp[j]==0:
    print('N',end=' ')
  else:
    print('Y',end=' ')