import sys
import heapq
#sys.stdin=open("input.txt","r")
n=int(sys.stdin.readline())
listfront=[]
listback=[]
mid=int(sys.stdin.readline())
print(mid)
for i in range(n-1):
  m=int(sys.stdin.readline())
  if m>mid:
    heapq.heappush(listback,m)
  else:
    heapq.heappush(listfront,-1*m)
  if len(listfront)==len(listback)+1:
    heapq.heappush(listback,mid)
    mid=heapq.heappop(listfront)*(-1)
  elif len(listfront)+2==len(listback):
    heapq.heappush(listfront,-1*mid)
    mid=heapq.heappop(listback)
  print(mid)
    
    
  