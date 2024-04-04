import sys
#sys.stdin=open("input.txt","r")
sys.setrecursionlimit(10**5)
def dfs(graph,k):
  global check,ans
  print(k,end=' ')
  check[k]=ans
  ans+=1
  for i in graph[k]:
    if check[i]==0:
      dfs(graph,i)

def bfs(graph,k):
  global check,queue,ans
  print(queue.pop(0),end=' ')
  for i in graph[k]:
    if check[i]==0:
      queue.append(i)
      check[i]=ans
      ans+=1
  if queue:
    bfs(graph,queue[0])
  
n,m,k=map(int,sys.stdin.readline().split())
check=[0]*(n+1)
ans=1
graph=[[] for _ in range(n+1)]
for i in range(m):
  a,b=map(int,sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)
for i in range(1,n+1):
  graph[i].sort()
dfs(graph,k)
for i in range(1,n+1):
  check[i]=0
print('')
ans=1
check[k]=ans
ans+=1
queue=[]
queue.append(k)
bfs(graph,queue[0])