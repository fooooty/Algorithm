import sys
from collections import deque
#sys.stdin=open("input.txt")
queue=deque()
n,m=map(int,sys.stdin.readline().split())
if n==m:
  print(0)
  exit()
check=[0]*(100001)
num=1
idx=n
queue.append(n)
while queue:
  check[idx]=num
  queue.popleft()
  for i in (idx+1,idx-1,idx*2):
    if 0<=i<(100001) and check[i]==0:
      queue.append(i)
      check[i]=num+1
      if i == m:
        print(check[m]-1)
        exit(0)
  if queue:
    num=check[queue[0]]
    idx=queue[0]