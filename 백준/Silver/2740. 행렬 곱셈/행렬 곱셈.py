import sys
#sys.stdin=open("input.txt","r")

def mult(list1,list2,n,m,k):
  ans=[[0]*k for i in range(n)]
  for i in range(n):
    for j in range(k):
      for l in range(m):
        ans[i][j]+=list1[i][l]*list2[l][j]
  return ans
      
list1=[]
list2=[]
n,m=map(int,sys.stdin.readline().split())
for i in range(n):
  list1.append(list(map(int,sys.stdin.readline().split())))
m,k=map(int,sys.stdin.readline().split())
for i in range(m):
  list2.append(list(map(int,sys.stdin.readline().split())))
ans=mult(list1,list2,n,m,k)
for i in range(n):
  for j in range(k):
    print(ans[i][j],end=' ')
  print('')