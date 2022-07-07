import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T) : 
    a, b = map(int, input().split())
    if a % 10 == 0 : 
        print(10)
        continue
    if b % 4 == 0 : 
        print((a**4)%10)
        continue
    print((a**(b%4))%10)
    
    
'''
1 1 1 1 --> 1
2 4 8 6 2 4 8 6 --> 4
3 9 7 1 3 9 7 1 --> 4
4 6 4 6 --> 2
5 5 5 5 --> 1
6 6 6 6 -> 1
7 9 3 1 7 9 3 1 --> 4
8 4 2 6 8 4 2 6 --> 4
9 1 9 1 --> 2
'''
