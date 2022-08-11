import sys

input = sys.stdin.readline()

dr = (0, 0, 1, -1)
dc = (1, -1, 0, 0)

def dfs(depth, r, c, percentage):
    global result
    if depth == N:
        result += percentage
        return
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if check[nr][nc]:
            continue
        check[nr][nc] = 1
        dfs(depth + 1, nr, nc, percentage * prob[i])
        check[nr][nc] = 0

N, e, w, s, n = map(int, input.split())
prob = [e / 100, w / 100, s / 100, n / 100]

result = 0
check = [[0] * (2 * N + 1) for _ in range(2 * N + 1)]
check[N][N] = 1

dfs(0, N, N, 1)

print(result)
