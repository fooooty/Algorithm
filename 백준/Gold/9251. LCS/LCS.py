import sys
#sys.stdin=open("input.txt","r")
a=list(sys.stdin.readline().rstrip())
b=list(sys.stdin.readline())
adynamic=[[0]*len(b) for i in range(len(a))]
aa=0
bb=0
for i in range(len(b)):
  if a[0]==b[i] or aa==1:
    adynamic[0][i]=1
    aa=1
for i in range(len(a)):
  if b[0]==a[i] or bb==1:
    adynamic[i][0]=1
    bb=1
for i in range(1,len(a)):
  for j in range(1,len(b)):
    if a[i]==b[j]:
      adynamic[i][j]=adynamic[i-1][j-1]+1
    else:
      adynamic[i][j]=max(adynamic[i-1][j],adynamic[i][j-1])
print(adynamic[len(a)-1][len(b)-1])