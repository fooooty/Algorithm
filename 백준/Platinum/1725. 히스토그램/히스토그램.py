import sys
#sys.stdin=open("input.txt","r")
n=int(sys.stdin.readline())
stack=[]
start=0
ans=0
for i in range(n+1):
  if i==n:
    a=0
  else: 
    a=int(sys.stdin.readline())
  start=i
  if stack:
    if stack[-1][1]<a:
      stack.append([start,a])
    else:
      while stack and stack[-1][1]>=a:
        start,ph=stack.pop()
        ans=max(ans,(i-start)*ph)
      stack.append([start,a])
  else:
    stack.append([start,a])
print(ans)