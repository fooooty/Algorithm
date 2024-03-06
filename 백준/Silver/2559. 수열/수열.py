import sys
#sys.stdin=open("input.txt","r")
n,m=map(int,sys.stdin.readline().split())
ssum=[0]*(n+1)
numlist=list(map(int,sys.stdin.readline().split()))
ssum[1]=numlist[0]
for i in range(1,n):
  ssum[i+1]=ssum[i]+numlist[i]
ans=-10e9
for i in range(m,n+1):
  ans=max(ans,ssum[i]-ssum[i-m])
print(ans)