import sys
input = sys.stdin.readline
N, M = map(int, input().split())
G = [0] + [[0]*(N+1) for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a][b] = 1
    G[b][a] = 1
dist = [0] + [[0]*(N+1) for _ in range(N)]
for i in range(1,N+1):
    for j in range(1,N+1):
        if i == j: dist[i][j] = 0
        elif G[i][j]: dist[i][j] = G[i][j]
        else:
            dist[i][j] = float('inf')
for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j]);
bacon = [float('inf')] + [sum(e) for e in dist[1:]]
print(bacon.index(min(bacon)))