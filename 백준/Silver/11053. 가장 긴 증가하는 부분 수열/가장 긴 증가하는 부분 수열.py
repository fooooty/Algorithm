import sys

#sys.stdin=open("input.txt","r")
n=int(sys.stdin.readline())
m=list(map(int,sys.stdin.readline().split()))
ans=[0]*n
ans[0]=1
maxx=-1
for i in range(1,n):
  ans[i]=1
  for j in range(0,i):
    if m[i]>m[j]:
      ans[i]=max(ans[i],ans[j]+1)
  maxx=max(maxx,ans[i])
maxx=max(maxx,ans[n-1])
print(maxx)