import sys
#sys.stdin=open("input.txt","r")
stack=[]
n=int(sys.stdin.readline().rstrip())
numlist=list(map(int,sys.stdin.readline().split()))
ans=[-1]*n
for i in range(n):
  if stack:
    if stack[-1][1]>numlist[i]:
      stack.append((i,numlist[i]))
    else:
      while stack:
        if stack[-1][1]<numlist[i] :
          ans[stack[-1][0]]=numlist[i]
          stack.pop()
        else:
          break
      stack.append((i,numlist[i]))
  else:
    stack.append((i,numlist[i]))
for i in ans:
  print(i,end=" ")