import sys
#sys.stdin=open("input.txt","r")
n=int(sys.stdin.readline())
line=list(map(int,sys.stdin.readline().split()))
price=list(map(int,sys.stdin.readline().split()))
current=price[0]
ans=0
for i in range(n-1):
  if current>price[i]:
    current=price[i]
  ans+=current*line[i]
print(ans)