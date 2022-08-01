import sys
from collections import deque
input = sys.stdin.readline
def BFS():
    q = deque([N])
    while q:
        x = q.popleft()
        if x == K:
            print(M[x])
            break
        for nx in (x-1, x+1, 2*x):
            if 0<=nx<=MAX and not M[nx]:
                M[nx] = M[x] + 1
                q.append(nx)

N, K = map(int, input().split())
MAX = 100000
M = [0] * (MAX+1)
BFS()