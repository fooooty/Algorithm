import sys
import heapq
#sys.stdin=open("input.txt","r")
heap=[]
n=int(sys.stdin.readline())
for i in range(n):
  x=int(sys.stdin.readline())
  if x==0:
    if heap:
      print(heapq.heappop(heap)[1])
    else:
      print(0)
  else:
    if x>0:
      heapq.heappush(heap,(x,x))
    else:
      heapq.heappush(heap,(-1*x,x))