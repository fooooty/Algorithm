import sys
#sys.stdin=open("input.txt","r")
  
def checkzero(x,y,scale):
  global paper
  for i in range(x,x+scale):
    for j in range(y,y+scale):
      if paper[i][j]==1:
        return 0
  return 1

def checkone(x,y,scale):
  global paper
  for i in range(x,x+scale):
    for j in range(y,y+scale):
      if paper[i][j]==0:
        return 0
  return 1
  
def split(x,y,scale):
  if scale==0:
    return
  if checkzero(x,y,scale)==1:
    print(0,end='')
  elif checkone(x,y,scale)==1:
    print(1,end='')
  else:
    print('(',end='')
    split(x,y,int(scale/2))
    split(x,y+int(scale/2),int(scale/2))
    split(x+int(scale/2),y,int(scale/2))
    split(x+int(scale/2),y+int(scale/2),int(scale/2))
    print(')',end='')
    
n=int(sys.stdin.readline())
paper=[]
for i in range(n):
  cnt=str(sys.stdin.readline().rstrip())
  paper.append(list(cnt))
  for j in range(n):
    paper[i][j]=int(paper[i][j])
split(0,0,n)