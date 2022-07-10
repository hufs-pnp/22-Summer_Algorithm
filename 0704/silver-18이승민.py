A = input().split('-')
num = []

for i in A:
    temp = 0
    add = list(map(int, i.split('+')))
    for j in add:
        temp += j
    num.append(temp)

result = num[0]
for i in range(1, len(num)):
    result -= num[i]

print(result)
