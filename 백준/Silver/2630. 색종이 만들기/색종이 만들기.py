import sys
#sys.stdin=open("input.txt","r")
ans=0
white=0
def allwhite(x,y,scale):
  global paper
  cnt=0
  for i in range(x,x+scale):
    for j in range(y,y+scale):
      if paper[i][j]==1:
        cnt=1
  if cnt==1:
    return 0
  return 1
  
def check(x,y,scale):
  global paper
  for i in range(x,x+scale):
    for j in range(y,y+scale):
      if paper[i][j]==0:
        return 0
  return 1
  
def split(x,y,scale):
  global ans,white
  if scale==0:
    return
  point=check(x,y,scale)
  if allwhite(x,y,scale)==1:
    white+=1
  elif point==0:
    split(x,y,int(scale/2))
    split(x+int(scale/2),y,int(scale/2))
    split(x+int(scale/2),y+int(scale/2),int(scale/2))
    split(x,y+int(scale/2),int(scale/2))
  else:
    ans+=1
    
n=int(sys.stdin.readline())
paper=[]
for i in range(n):
  paper.append(list(map(int,sys.stdin.readline().split())))
split(0,0,n)
print(white)
print(ans)