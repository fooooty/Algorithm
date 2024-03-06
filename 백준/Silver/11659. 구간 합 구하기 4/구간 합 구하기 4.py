import sys
#sys.stdin=open("input.txt","r")
n,m=map(int,sys.stdin.readline().split())
ssum=[0]*(n+1)
numlist=list(map(int,sys.stdin.readline().split()))
ssum[1]=numlist[0]
for i in range(1,n):
  ssum[i+1]=ssum[i]+numlist[i]
for i in range(m):
  a,b=map(int,sys.stdin.readline().split())
  print(ssum[b]-ssum[a-1])