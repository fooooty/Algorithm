import sys
#sys.stdin=open("input.txt","r")
n,m=map(int,sys.stdin.readline().split())
graph=[[]for i in range(n+1)]
ans=[10e9]*(n+1)
for i in range(m):
  a,b,c=map(int,sys.stdin.readline().split())
  graph[a].append((b,c))
ans[1]=0
for i in range(n-1):
  for j in range(1,n+1):
    if ans[j]!=10e9:
      for k in graph[j]:
        if ans[k[0]]>(ans[j]+k[1]):
          ans[k[0]]=ans[j]+k[1]
check=0
for j in range(1,n+1):
  if ans[j]!=10e9:
    for k in graph[j]:
      if ans[k[0]]>(ans[j]+k[1]):
        check=1
        ans[k[0]]=ans[j]+k[1]
if check==1:
  print(-1)
  exit(0)
for i in range(2,n+1):
  if ans[i]==10e9:
    print(-1)
  else:
    print(ans[i])