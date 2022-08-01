import sys
input = sys.stdin.readline

def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

def find(x):
    if parent[x] != x:
        return find(parent[x])
    return parent[x]

N, M = map(int, input().split())
edges = []
for _ in range(M):
    edges.append([int(m) for m in input().split()])
edges.sort(key = lambda x: x[2])
parent = list(range(N+1))
cost = []
for A, B, C in edges:
    if find(A) != find(B):
        cost.append(C)
        union(A, B)
print(sum(cost[:-1]))
