import sys
#sys.stdin=open("input.txt","r")
def mid(graph,label,len):
  pivotleft=label
  pivotright=label
  height=graph[label]
  ans=graph[label]
  while True:
    if graph[pivotleft-1]==0 and graph[pivotright+1]==0:
      break
    if graph[pivotleft-1]>=graph[pivotright+1]:
      pivotleft-=1
      height=min(height,graph[pivotleft])
      ans=max(ans,height*(pivotright-pivotleft+1))
    else:
      pivotright+=1
      height=min(height,graph[pivotright])
      ans=max(ans,height*(pivotright-pivotleft+1))
  return ans
    
def split(graph,len):
  if len==1:
    return graph[1]
  label=(len)//2
  left=split([0]+graph[1:label+1]+[0],label)
  right=split([0]+graph[label+1:len+1]+[0],len-label)
  middle=mid(graph,label,len)
  return max(max(left,right),middle)
n=int(sys.stdin.readline())
graph=[]
for i in range(n):
  graph.append(int(sys.stdin.readline()))
print(split([0]+graph+[0],n))