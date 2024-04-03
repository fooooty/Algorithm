import sys
sys.setrecursionlimit(10**5)
#sys.stdin=open("input.txt","r")
def bfs(maplist,r):
  global check,visitlist,ans
  visitlist.pop(0)
  for i in maplist[r]:
    if check[i]==0:
      visitlist.append(i)
      check[i]=ans
      ans+=1
  if visitlist:
    bfs(maplist,visitlist[0])
n,m,r=map(int,sys.stdin.readline().split())
maplist=[[] for i in range(n+1)]
visitlist=[]
ans=1
check=[0]*(n+1)
for i in range(m):
  a,b=map(int,sys.stdin.readline().split())
  maplist[a].append(b)
  maplist[b].append(a)
for i in range(n+1):
  maplist[i]=sorted(maplist[i])
visitlist.append(r)
check[r]=ans
ans+=1
bfs(maplist,r)
for i in range(1,n+1):
  print(check[i])