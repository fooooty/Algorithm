import sys
#sys.stdin=open("input.txt","r")
def change(target,start,end,ans):
  global changex
  if start>end:
    return
  label=(start+end)//2
  if ans[label]>=target:
    changex=min(changex,label)
    change(target,start,label-1,ans)
  else:
    change(target,label+1,end,ans)
n=int(sys.stdin.readline())
numlist=list(map(int,sys.stdin.readline().split()))
ans=[]
ans.append(numlist[0])
for i in range(1,n):
  changex=10e9
  if ans[len(ans)-1]<numlist[i]:
    ans.append(numlist[i])
  else:
    change(numlist[i],0,len(ans)-1,ans)
    ans[changex]=numlist[i]
print(len(ans))