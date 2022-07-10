x=input().split('-')
total=[]
for i in x:
    y=0
    z=i.split('+')
    for j in z:
        y+=int(j)
    total.append(y)
a=total[0]
for i in range(1,len(total)):
    a-=total[i]
print(a)
