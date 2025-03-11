import sys
sys.setrecursionlimit(100000)
#sys.stdin=open("/Users/sonjiyeon/Desktop/algorithm/input.txt","r")
def findmom(x,unionfind):
    if x==unionfind[x]:
        return x
    unionfind[x]=findmom(unionfind[x],unionfind)
    return unionfind[x]

n,m=map(int,sys.stdin.readline().split())
unionfind=[i for i in range(n+1)] 
for i in range(m):
    code,a,b=map(int,sys.stdin.readline().split())
    amom=findmom(a,unionfind)
    bmom=findmom(b,unionfind)
    if code==0:
        if amom!=bmom:
            if amom<bmom:
                unionfind[bmom]=amom
            else:
                unionfind[amom]=bmom
    else:
        if amom!=bmom:
            print("NO")
        else:
            print("YES")
