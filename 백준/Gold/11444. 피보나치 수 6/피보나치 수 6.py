import sys
#sys.stdin=open("input.txt","r")
def multmatrix(a,b,n,m,k):
  global p
  ans=[[0]*k for i in range(n)]
  for i in range(n):
    for j in range(k):
      for l in range(m):
        ans[i][j]+=(a[i][l]*b[l][j])%p
  return ans
def fibo(a,n):
  if n==1:
    return a
  tmp=fibo(a,n//2)
  ans=multmatrix(tmp,tmp,2,2,2)
  if n%2==1:
    ans=multmatrix(ans,a,2,2,2)
  return ans
p=10**9+7
a=[[1,1],[1,0]]
u=[[1],[0]]
n=int(sys.stdin.readline())
ans=multmatrix(fibo(a,n),u,2,2,1)
print(ans[1][0])