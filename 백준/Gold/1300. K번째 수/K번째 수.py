import sys
#sys.stdin=open("input.txt","r")
def binary(start,end):
  global n,min,ans
  if start>end:
    return
  label=(start+end)//2
  cnt=0
  for i in range(1,n+1):
    if i*n<=label:
      cnt+=n
    else:
      cnt+=(label//i)
  if cnt>=m:
    ans=min(ans,label)
    binary(start,label-1)
  else:
    binary(label+1,end)

ans=10e9
n=int(sys.stdin.readline())
m=int(sys.stdin.readline())
binary(1,n*n)
print(ans)
