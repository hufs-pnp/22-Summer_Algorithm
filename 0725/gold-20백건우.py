import sys
input = sys.stdin.readline

class UnionFind:

    def __init__(self, V):
        self.array = list(range(V+1))

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x <= y:
            self.array[y] = x
        else:
            self.array[x] = y

    def find(self, x):
        if self.array[x] != x:
            return self.find(self.array[x])
        return x

V, E = map(int, input().split())
edges = []
for _ in range(E):
    edges.append([int(e) for e in input().split()])
edges.sort(key = lambda x: x[2])
vertex = UnionFind(V)
weight = 0
edge = 0
for A, B, C in edges:
    if vertex.find(A) != vertex.find(B):
        weight += C
        edge += 1
        vertex.union(A,B)
    if edge == E-1:
        break
print(weight)