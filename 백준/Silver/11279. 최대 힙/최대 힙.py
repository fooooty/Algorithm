import sys
#sys.stdin=open("input.txt","r")
heap=[0]
n=int(sys.stdin.readline())
def arrange(label):
  global heap
  if label==1:
    return
  tmp=0
  if heap[label]>heap[label//2]:
    tmp=heap[label]
    heap[label]=heap[label//2]
    heap[label//2]=tmp
    arrange(label//2)
  return
  
def heappop(label):
  global heap
  if label*2>len(heap)-1:
    return
  left=label*2
  right=label*2+1
  if right>len(heap)-1:
    right=left
  compare=max(heap[left],heap[right])
  if compare==heap[left] and compare>heap[label]:
    heap[label],heap[left]=heap[left],heap[label]
    heappop(left)
  elif compare==heap[right] and compare>heap[label]:
    heap[label],heap[right]=heap[right],heap[label]
    heappop(right)
    
for i in range(n):
  x=int(sys.stdin.readline())
  if x!=0:
    heap.append(x)
    label=len(heap)-1
    arrange(label)
  else:
    if len(heap)==1:
      print(0)
    elif len(heap)==2:
      print(heap.pop(1))
    else:
      print(heap[1])
      heap[1]=heap[-1]
      del heap[-1]
      heappop(1)
