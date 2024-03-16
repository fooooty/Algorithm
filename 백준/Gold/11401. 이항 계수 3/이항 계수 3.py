import sys
#sys.stdin=open("input.txt","r")
def fact(n):
  global p
  ans=1
  for i in range(n):
    ans*=(i+1)
    ans%=p
  return int(ans)
def zegop(n,k):
  global p
  if k==1:
    return n
  ans=zegop(n,int(k/2))
  if k%2==0:
    return (ans*ans)%p
  else:
    return (ans*ans*n)%p
p=1000000007
n,k=map(int,sys.stdin.readline().split())
top=fact(n)
bottom=zegop((fact(n-k)*fact(k)),p-2)%p
print((top*bottom)%p)