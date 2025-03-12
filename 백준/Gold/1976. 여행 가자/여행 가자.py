import sys
sys.setrecursionlimit(100000)
#sys.stdin=open("/Users/sonjiyeon/Desktop/algorithm/input.txt","r")
def findmom(x,unionfind):
    if x==unionfind[x]:
        return x
    unionfind[x]=findmom(unionfind[x],unionfind)
    return unionfind[x]

n=int(sys.stdin.readline())
m=int(sys.stdin.readline())
unionfind=[i for i in range(n)] 
for i in range(n):
    linkmap=list(map(int,sys.stdin.readline().split()))
    amom=findmom(i,unionfind)
    for idx,j in enumerate(linkmap):
        if j==1:
            bmom=findmom(idx,unionfind)
            if amom!=bmom:
                if amom<bmom:
                    unionfind[bmom]=amom
                else:
                    unionfind[amom]=bmom
    #print(unionfind)
visit=list(set(list(map(int,sys.stdin.readline().split()))))

amom=findmom(visit[0]-1,unionfind)
for i in range(1,len(visit)):
    bmom=findmom(visit[i]-1,unionfind)
    if amom!=bmom:
        print("NO")
        exit(0)
print("YES")