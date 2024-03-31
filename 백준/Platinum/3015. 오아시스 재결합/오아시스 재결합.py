import sys

#sys.stdin = open("input.txt", "r")
n = int(sys.stdin.readline().rstrip())
ans = 0
stack=[]
for i in range(n):
  m = int(sys.stdin.readline())
  check=0
  while stack:
    if stack[-1][0] < m:
      ans += stack[-1][1]
      stack.pop()
    elif stack[-1][0] == m:
      stack[-1][1]+=1
      check=1
      break
    else:
      break
  if check==0:
    stack.append([m,1])
  if len(stack)!=1 or stack[-1][1]!=1:
    if stack[-1][1]!=1:
      ans+=(stack[-1][1]-1)
      if len(stack)>=2:
        ans+=1
    else:
      ans+=1
print(ans)
