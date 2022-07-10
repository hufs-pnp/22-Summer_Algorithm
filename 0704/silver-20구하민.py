s = input().split('-')

arr = []

for i in s : 
    t = i.split('+')
    n = 0
    for j in t : 
        n += int(j)
    
    arr.append(n)

num = arr[0]

for i in range(1, len(arr)) : 
    num -= arr[i]
print(num)
