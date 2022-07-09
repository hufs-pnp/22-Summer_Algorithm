import sys
n=int(sys.stdin.readline())

inp=[]
for i in range(n):
    x,y=map(int,sys.stdin.readline().split())
    x%=10
    if x!=0:
        jari = []
        temp=x
        while jari==[] or temp!=jari[0]:
            jari.append(temp)
            temp=(temp*x)%10
        y%=len(jari)
        print(jari[y-1])
    else:print(10)
