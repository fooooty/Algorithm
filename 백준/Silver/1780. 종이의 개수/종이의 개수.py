import sys
#sys.stdin=open("input.txt","r")
ans=[0]*3
def checknum(x,y,scale,num):
  global paper
  for i in range(x,x+scale):
    for j in range(y,y+scale):
      if paper[i][j]!=num:
        return 0
  return 1

def split(x,y,scale):
  global ans
  for i in range(-1,2,1):
    if checknum(x,y,scale,i)==1:
      ans[i+1]+=1
      return
  split(x,y,int(scale/3))
  split(x,y+int(scale/3),int(scale/3))
  split(x,y+2*int(scale/3),int(scale/3))
  split(x+int(scale/3),y,int(scale/3))
  split(x+int(scale/3),y+int(scale/3),int(scale/3))
  split(x+int(scale/3),y+2*int(scale/3),int(scale/3))
  split(x+2*int(scale/3),y,int(scale/3))
  split(x+2*int(scale/3),y+int(scale/3),int(scale/3))
  split(x+2*int(scale/3),y+2*int(scale/3),int(scale/3))
    
n=int(sys.stdin.readline())
paper=[]
for i in range(n):
  paper.append(list(map(int,sys.stdin.readline().split())))
split(0,0,n)
for i in ans:
  print(i)