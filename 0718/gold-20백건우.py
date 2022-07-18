import sys
from itertools import combinations
input = sys.stdin.readline

N, K = map(int, input().split())
words = [set(input().rstrip()[4:-4])-set('acint') for _ in range(N)]
if K < 5:
    print(0)
    sys.exit()
if K == 26:
    print(N)
    sys.exit()
ans = 0
for SET in map(set,combinations(set(chr(i) for i in range(97, 123))-set('acint'), K-5)):
    cnt = 0
    for w in words:
        if w.issubset(SET):
            cnt += 1
    ans = max(ans, cnt)
print(ans)