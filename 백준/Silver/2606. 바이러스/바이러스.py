import sys
#sys.stdin=open("input.txt","r")
def dfs(maplist,k):
  global visit,ans
  visit[k]=1
  ans+=1
  for i in maplist[k]:
    if visit[i]==0:
      dfs(maplist,i)

n=int(sys.stdin.readline())
maplist=[[] for i in range(n+1)]
visit=[0]*(n+1)
m=int(sys.stdin.readline())
ans=0
for i in range(m):
  a,b=map(int,sys.stdin.readline().split())
  maplist[a].append(b)
  maplist[b].append(a)
dfs(maplist,1)
print(ans-1)