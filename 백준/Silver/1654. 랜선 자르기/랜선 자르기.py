import sys
#sys.stdin=open("input.txt","r")
def binary(start,end,have):
  if start>end:
    return
  global m,result
  label=(start+end)//2
  ans=0
  for i in have:
    ans+=(i//label)
  if ans>=m:
    result=max(result,label)
    binary(label+1,end,have)
  elif ans<m:
    binary(start,label-1,have)
n,m=map(int,sys.stdin.readline().split())
have=[]
tmp=0
result=0
for i in range(n):
  have.append(int(sys.stdin.readline()))
  tmp=max(tmp,have[i])
binary(1,tmp,have)
print(result)