import sys
from collections import deque
#sys.stdin=open("input.txt","r")
k=int(sys.stdin.readline())
for i in range(k):
  v,e=map(int,sys.stdin.readline().split())
  graph=[[] for _ in range(v+1)]
  empty=[]
  for j in range(e):
    empty=list(map(int,sys.stdin.readline().split()))
    graph[empty[0]].append(empty[1])
    graph[empty[1]].append(empty[0])
  queue=deque()
  check=[0]*(v+1)
  queue.append((1,1))
  check[1]=1
  ans=0
  while True:
    if queue:
      x,color=queue.popleft()
      color=(-1*color)
      for k in graph[x]:
        if check[k]==0:
          check[k]=color
          queue.append((k,color))
        elif check[k]!=color:
          ans=1
    else:
      for i in range(1,v+1):
        if check[i]==0 and len(graph[i])!=0:
          queue.append((i,1))
          check[i]=1
          break
      if not queue:
        break
  if ans==1:
    print('NO')
  else:
    print('YES')