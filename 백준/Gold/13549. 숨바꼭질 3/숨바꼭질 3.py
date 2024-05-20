import sys
from collections import deque
def findway(idx,final):
  global n,m
  queue=deque()
  ans=[10e9]*(max(n+1,m+3))
  check=[0]*(max(n+1,m+3))
  ans[idx]=0
  nextidx=(idx,0)
  queue.append((idx,0))
  while True:
    idx=(queue.popleft()[0])
    if check[idx]==0:
      check[idx]=1
      nextidx=(0,10e9)
      if idx==final:
        return ans[final]
      if idx*2<=m+2 and check[idx*2]==0:
        ans[idx*2]=min(ans[idx*2],ans[idx])
        queue.append((idx*2,ans[idx*2]))
      if idx+1<=m and check[idx+1]==0:
        ans[idx+1]=min(ans[idx+1],ans[idx]+1)
        queue.append((idx+1,ans[idx+1]))
      if idx-1>=0 and check[idx-1]==0:
        ans[idx-1]=min(ans[idx-1],ans[idx]+1)
        queue.append((idx-1,ans[idx-1]))


#sys.stdin=open("input.txt","r")
n,m=map(int,sys.stdin.readline().split())
print(findway(n,m))