import sys
import math
#sys.stdin=open("input.txt","r")
n,m=map(int,sys.stdin.readline().split())
numlist=[]
for i in range(n):
  numlist.append(int(sys.stdin.readline()))
  if numlist[len(numlist)-1]>m:
    del numlist[len(numlist)-1]
ans=0
for i in range(len(numlist)-1,0,-1):
  ans+=int(m/numlist[i])
  m=m%numlist[i]
print(ans+m)