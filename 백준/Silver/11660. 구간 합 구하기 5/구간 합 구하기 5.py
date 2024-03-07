import sys
import math
#sys.stdin=open("input.txt","r")
n,m=map(int,sys.stdin.readline().split())
sumlist=[[0]*(n+1) for i in range(n+1)]
numlist=[]
for i in range(n):
  numlist.append(list(map(int,sys.stdin.readline().rstrip().split())))
  for j in range(n):
    sumlist[i+1][j+1]=numlist[i][j]+sumlist[i+1][j]
for i in range(m):
  ans=0
  a,b,c,d=map(int,sys.stdin.readline().rstrip().split())
  for j in range(a,c+1):
    ans+=sumlist[j][d]-sumlist[j][b-1]
  print(ans)