T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    x = a % 10
    if x == 1 or x == 5 or x == 6:
        print(x)
    elif x == 0:
        print(10)
    elif x == 4:
        y = b % 2
        li = [6, 4]
        print(li[y])
    elif x == 9:
        y = b % 2
        li = [1, 9]
        print(li[y])
    elif x == 2:
        y = b % 4
        li = [6, 2, 4, 8]
        print(li[y])
    elif x == 3:
        y = b % 4
        li = [1, 3, 9, 7]
        print(li[y])
    elif x == 7:
        y = b % 4
        li = [1, 7, 9, 3]
        print(li[y])
    elif x == 8:
        y = b % 4
        li = [6, 8, 4, 2]
        print(li[y])
