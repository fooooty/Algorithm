import math
import sys
#sys.stdin=open("input.txt","r")
dict={}
n=int(sys.stdin.readline())
Have=list(map(int,sys.stdin.readline().split()))
for i in Have:
  if i not in dict:
    dict[i]=1
  else:
    dict[i]+=1
m=int(sys.stdin.readline())
Get=list(map(int,sys.stdin.readline().split()))
for i in Get:
  if i in dict:
    print(dict[i],end=' ')
  else:
    print(0,end=' ')