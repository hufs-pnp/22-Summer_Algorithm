n = input().split('-')
n[0] = sum(map(int,n[0].split('+')))

for i in range(1,len(n)):
    n[i] = -sum(map(int,n[i].split('+')))

print(sum(n))
