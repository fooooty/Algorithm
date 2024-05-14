import sys
def findway(idx,final):
  global graph
  check=[0]*(n+1)
  ans=[10e9]*(n+1)
  nextidx=(idx,0)
  ans[idx]=0
  exitt=0
  while True:
    idx=nextidx[0]
    check[idx]=1
    if idx == final:
      return ans[final]
    for i in graph[idx]:
      if check[i[0]]==0:
        ans[i[0]]=min(ans[i[0]],ans[idx]+i[1])
    exitt=0
    nextidx=(0,10e9)
    for i in range(1,n+1):
      if check[i]==0 and ans[i]<nextidx[1] and ans[i]!=10e9:
        exitt=1
        nextidx=(i,ans[i])
    if exitt==0:
      break
  return -1
    
#sys.stdin=open("input.txt","r")
n,m=map(int,sys.stdin.readline().split())
graph=[[] for i in range(n+1)]
for i in range(m):
  a,b,c=map(int,sys.stdin.readline().split())
  graph[a].append((b,c))
  graph[b].append((a,c))
a,b=map(int,sys.stdin.readline().split())
firsta=findway(1,a)
second=findway(a,b)
thirda=findway(b,n)
firstb=findway(1,b)
thirdb=findway(a,n)
realans=10e9
if firsta!=-1 and second!=-1 and thirda!=-1:
  realans=firsta+second+thirda
if firstb!=-1 and second!=-1 and thirdb!=-1:
  realans=min(realans,firstb+second+thirdb)
if realans==10e9:
  print(-1)
else:
  print(realans)