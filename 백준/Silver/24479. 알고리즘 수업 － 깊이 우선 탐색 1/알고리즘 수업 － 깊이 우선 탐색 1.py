import sys
sys.setrecursionlimit(10**5)
def dfs(n,node,k):
  global visit,ans
  visit[k]=ans
  ans+=1
  for i in node[k]:
    if visit[i]==0:
      dfs(n,node,i)
#sys.stdin = open("input.txt", "r")
n,m,k = map(int,sys.stdin.readline().split())
visit=[0]*(n+1)
node=[[] for i in range(n+1)]
ans=1
for i in range(m):
  a,b=map(int,sys.stdin.readline().split())
  node[a].append(b)
  node[b].append(a)
node=[sorted(i) for i in node ]
dfs(n,node,k)
for i in range(1,n+1):
  print(visit[i])