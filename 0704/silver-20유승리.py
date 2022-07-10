import sys

ex = list(sys.stdin.readline().strip().split('-'))

result = 0
for i in ex[0].split('+'):
    result += int(i)
    
for i in ex[1:]:
    for j in i.split('+'):
        result -= int(j)
        
print(result)
