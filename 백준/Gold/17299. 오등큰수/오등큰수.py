import sys
#sys.stdin=open("input.txt","r")
stack=[]
n=int(sys.stdin.readline().rstrip())
numlist=list(map(int,sys.stdin.readline().split()))
count={}
ans=[-1]*n
for i in range(n):
  if numlist[i] in count.keys():
    count[numlist[i]]+=1
  else:
    count[numlist[i]]=1
for i in range(n):
  while stack:
    if count[stack[-1][1]]<count[numlist[i]]:
      ans[stack.pop()[0]]=numlist[i]
    else:
      break
  stack.append((i,numlist[i]))
for i in ans:
  print(i,end=" ")