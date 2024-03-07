import sys
import math
#sys.stdin=open("input.txt","r")
n,m=map(int,sys.stdin.readline().split())
numlist=list(map(int,sys.stdin.readline().split()))
summ=[0]*(n+1)
check=[0]*m
ans=0
for i in range(n):
  numlist[i]%=m
for i in range(1,n+1):
  summ[i]=(summ[i-1]+numlist[i-1])%m
  check[summ[i]]+=1
  if summ[i]==0:
    ans+=1
for i in range(m):
  if check[i]>1:
    ans+=math.comb(check[i],2)
print(ans)