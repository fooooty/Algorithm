import sys
#sys.stdin=open("input.txt","r")

def mult(list1,list2):
  global n
  ans=[[0]*n for i in range(n)]
  for i in range(n):
    for j in range(n):
      for l in range(n):
        ans[i][j]+=(list1[i][l]*list2[l][j])%1000
  return ans

def pre(list1,m):
  global n
  if m==1:
    return list1
  elif m==2:
    return mult(list1,list1)
  numarr=pre(list1,int(m/2))
  ansarr=mult(numarr,numarr)
  if m%2==0:
    return ansarr
  else:
    return mult(ansarr,list1)
  
list1=[]
n,m=map(int,sys.stdin.readline().split())
for i in range(n):
  list1.append(list(map(int,sys.stdin.readline().split())))
ans=pre(list1,m)
for i in range(n):
  for j in range(n):
    print(ans[i][j]%1000,end=" ")
  print('')