import sys
#sys.stdin=open("input.txt","r")
ans=1
for i in range(3):
  n=int(sys.stdin.readline())
  ans*=n
count=[0]*10
while True:
  if ans==0:
    break
  tt=int(ans%10)
  count[tt]=count[tt]+1
  ans=int(ans/10)
for i in count:
  print(i)