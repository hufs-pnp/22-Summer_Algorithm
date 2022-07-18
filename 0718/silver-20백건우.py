import sys

input = sys.stdin.readline
n = int(input())
#P[i][c]는 i번째 집을 c색으로 칠했을 때 최소 비용
P = [[0 for j in range(3)] for i in range(n+1)]

rgb = [int(e) for e in input().rstrip('\n').split()]
for i in range(3):
    P[1][i] = rgb[i]
for i in range(2,n+1):
    rgb = [int(e) for e in input().rstrip('\n').split()]
    for c in range(3): #c는 i번째 집에 칠할 색
        cost = 1001*i
        for j in range(3): #j는 i-1번째 집에 칠한 색
            if c == j:
                continue
            if P[i-1][j] < cost:
                cost = P[i-1][j]
        P[i][c] = cost + rgb[c]
print(min(P[n]))
