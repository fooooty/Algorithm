import sys
from collections import deque
event=[]
check=[0]*101
queue=deque()
#sys.stdin=open("input.txt","r")
n,m=map(int,sys.stdin.readline().split())
for i in range(n+m):
  event.append(list(map(int,sys.stdin.readline().split())))
queue.append(1)
check[1]=1
while queue:
  idx=queue.popleft()
  for i in range(1,7):
    if idx+i>100:
      break
    if check[idx+i]==0:
      if idx+i==100:
        print(check[idx])
        exit()
      add=0
      check[idx+i]=check[idx]+1
      for j in event:
        if j[0]==(idx+i):
          add=1
          if check[j[1]]==0:
            check[j[1]]=check[idx]+1
          queue.append(j[1])
      if add==0:
        queue.append(idx+i)