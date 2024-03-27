import sys
import heapq
#sys.stdin=open("input.txt","r")
heap=[]
n=int(sys.stdin.readline())
for i in range(n):
  x=int(sys.stdin.readline())
  if x==0:
    if heap:
      print(heapq.heappop(heap))
    else:
      print(0)
  else:
    heapq.heappush(heap,x)
