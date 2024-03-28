import sys
#sys.stdin=open("input.txt","r")
stack=[]
n=list(sys.stdin.readline().rstrip())
bomb=list(sys.stdin.readline().rstrip())
for i in n:
  stack.append(i)
  if len(stack)>=len(bomb) and stack[(len(stack)-len(bomb)):]==bomb:
    for j in range(len(bomb)):
      stack.pop()
if stack:
  for i in stack:
    print(i,end="")
else:
  print("FRULA")
