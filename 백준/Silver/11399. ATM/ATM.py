import sys
#sys.stdin=open("input.txt","r")
n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().rstrip().split()))
a.sort()
sum=0
for i in range(n):
  sum+=(a[i]*(n-i))
print(sum)