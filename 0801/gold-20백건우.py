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
    A, B, C = map(int, input().split())
    edges.append([C, A, B])
edges.sort()
parent = list(range(N+1))
cost = []
for C, A, B in edges:
    if find(A) != find(B):
        union(A, B)
        cost.append(C)
print(sum(cost[:-1]))
print(cost)