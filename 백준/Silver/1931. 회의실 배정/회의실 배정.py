import sys
import math
#sys.stdin=open("input.txt","r")
n=int(sys.stdin.readline())
res=[]
for i in range(n):
  res.append(list(map(int,sys.stdin.readline().rstrip().split())))
res.sort(key=lambda x:(x[1],x[0]))
ans=1
end=res[0][1]
for i in range(1,n):
  if end<=res[i][0]:
    ans+=1
    end=res[i][1]
print(ans)