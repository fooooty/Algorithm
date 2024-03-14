import sys
#sys.stdin=open("input.txt","r")

def multiple(a,b,c):
  if b==1:
    return a%c
  num=multiple(a,int(b/2),c)
  if b%2==0:
    return (num*num)%c
  else:
    return (num*num*a)%c
    
a,b,c=map(int,sys.stdin.readline().split())
print(multiple(a,b,c))