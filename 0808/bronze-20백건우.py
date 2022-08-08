import sys
input = sys.stdin.readline
ans = 0
curr = 0
for _ in range(4):
    A, B = map(int, input().split())
    curr += -A+B
    ans = max(ans, curr)
print(ans)