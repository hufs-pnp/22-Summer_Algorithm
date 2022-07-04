for i in range(int(input())):
    x,y = map(int, input().split())
    x = x%10; y = y%4+4
    result = x**y%10
    if result == 0: print(10)
    else: print(result)
