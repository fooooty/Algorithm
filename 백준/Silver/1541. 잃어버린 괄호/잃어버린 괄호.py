import sys
#sys.stdin=open("input.txt","r")
a=list(sys.stdin.readline().split("-"))
ans=0
ans+=sum(list(map(int,a[0].split('+'))))
for i in range(1,len(a)):
  ans-=sum(list(map(int,a[i].split('+'))))
print(ans)