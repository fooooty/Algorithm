import sys
#sys.stdin=open("input.txt","r")
def binary(start,end,have):
  global result
  if start>end:
    return
  global m,result
  label=(start+end)//2
  ans=0
  for i in have:
    if i>label:
      ans+=(i-label)
  if ans>=m:
    result=max(result,label)
    binary(label+1,end,have)
  else:
    binary(start,label-1,have)
    
n,m=map(int,sys.stdin.readline().split())
have=list(map(int,sys.stdin.readline().split()))
result=0
tmp=0
for i in have:
  tmp=max(tmp,i)
binary(1,tmp,have)
print(result)