import sys
from collections import deque

input = sys.stdin.readline()

n, k = map(int, input.split())
visited = [0] * 100001
que = deque([n])

while que:
    x = que.popleft()
    
    if x == k:  break
    
    elif ((x + 1) <= 100000) and (visited[x + 1] == 0):
        visited[x + 1] = visited[x] + 1
        que.append(x + 1)
        if (x + 1) == k:
            break
        
    if (0 <= x - 1) and (visited[x - 1] == 0):
        visited[x - 1] = visited[x] + 1
        que.append(x - 1)
        if (x - 1) == k:
            break
        
    if ((x * 2) <= 100000) and (visited[x * 2] == 0):
        visited[x * 2] = visited[x] + 1
        que.append(x * 2)
        if (x * 2) == k:
            break

print(visited[k])
