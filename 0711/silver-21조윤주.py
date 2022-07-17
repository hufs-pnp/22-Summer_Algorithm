import sys
n=int(sys.stdin.readline())
x,y=map(int,sys.stdin.readline().split())
lst=[None]*n
m=int(sys.stdin.readline())

def canFind(l,x,y):
    xpar,ypar=[x-1],[y-1]
    nextx,nexty=x-1,y-1
    while l[nextx]!=None:
        nextx=l[nextx]
        xpar.append(nextx)
    while l[nexty]!=None:
        nexty=l[nexty]
        ypar.append(nexty)
    if xpar[-1]==ypar[-1]:
        for i in range(len(xpar)):
            for j in range(len(ypar)):
                if xpar[i]==ypar[j]:
                    return i+j
    else:return -1

for i in range(m):
    p,s=map(int,sys.stdin.readline().split())
    lst[s-1]=p-1

print(canFind(lst,x,y))
