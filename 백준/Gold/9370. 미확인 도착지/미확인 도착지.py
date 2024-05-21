import sys
from collections import deque
#sys.stdin=open("input.txt","r")
def findway(s,e,graph):
  global n
  check=[0]*(n+1)
  ans=[10e9]*(n+1)
  nextidx=(s,0)
  ans[s]=0
  while True:
    index=nextidx[0]
    nextidx=(0,10e9) 
    check[index]=1
    if index==e:
      return ans[e]
    for k in graph[index]:
      if check[k[0]]==0:
        ans[k[0]]=min(ans[index]+k[1],ans[k[0]])
    cnt=0
    for k in range(1,n+1):
      if check[k]==0 and nextidx[1]>ans[k] and ans[k]!=10e9:
        cnt=1
        nextidx=(k,ans[k])
    if cnt==0:
      break
  return -1

T=int(sys.stdin.readline())
for i in range(T):
  n,m,t=map(int,sys.stdin.readline().split())
  graph=[[]for _ in range(n+1)]
  s,g,h=map(int,sys.stdin.readline().split())
  for j in range(m):
    a,b,d=map(int,sys.stdin.readline().split())
    if (a==g and b==h) or (a==h and b==g):
      point=d
    graph[a].append((b,d))
    graph[b].append((a,d))
  lili=[]
  for j in range(t):
    x=int(sys.stdin.readline())
    short=findway(s,x,graph)
    find=10e9
    xxx=findway(s,g,graph)
    yyy=findway(h,x,graph)
    if xxx!=-1 and yyy!=-1:
      find=xxx+yyy+point
    xxx=findway(s,h,graph)
    yyy=findway(g,x,graph)
    if xxx!=-1 and yyy!=-1:
      find=min(find,xxx+yyy+point)
    if short==find:
      lili.append(x)
  lili.sort()
  for j in lili:
    print(j,end=' ')
  print('')
    