import sys
#sys.stdin=open("input.txt","r")
def binary_search(start,end,graph,k):
  global ans
  if start>end:
    return
  label=(start+end)//2
  pivot=0
  cnt=1
  for i in range(1,n):
    if graph[i]-graph[pivot]>=label:
      pivot=i
      cnt+=1
  if cnt>=k:
    ans=max(ans,label)
    binary_search(label+1,end,graph,k)
  else:
    binary_search(start,label-1,graph,k)
ans=0
n,k=map(int,sys.stdin.readline().split())
graph=[]
for i in range(n):
  graph.append(int(sys.stdin.readline()))
graph.sort()
binary_search(1,(graph[n-1]-graph[0]+1)//(k-1),graph,k)
print(ans)