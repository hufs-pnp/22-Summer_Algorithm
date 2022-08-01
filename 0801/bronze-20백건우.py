import sys
input = sys.stdin.readline
def find_n(N):
    for n in range(1,N+1):
        if n*(n+1)//2 >= N:
            return n

A, B = map(int, input().split())
a, b = find_n(A), find_n(B)
aa = a*(a+1)//2
bb = b*(b+1)//2
print((bb*(2*b+1)//3-(bb-B)*b)-(aa*(2*a+1)//3-(aa-A)*a)+a)