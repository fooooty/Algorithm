import sys
#sys.stdin=open("input.txt","r")
def find(i,start,end,mlist):
  if start>end:
    return 0
  label=start+(end-start)//2
  if mlist[label]==i:
    return 1
  elif mlist[label]>i:
    if find(i,start,label-1,mlist):
      return 1
  else:
    if find(i,label+1,end,mlist):
      return 1
  return 0
m=int(sys.stdin.readline())
mlist=list(map(int,sys.stdin.readline().split()))
n=int(sys.stdin.readline())
nlist=list(map(int,sys.stdin.readline().split()))
mlist.sort()
for i in nlist:
  if find(i,0,m-1,mlist):
    print(1)
  else:
    print(0)