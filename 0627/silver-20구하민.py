from collections import deque
from sys import stdin

deq = deque([])
n = int(input())

for _ in range(n) : 
    c = stdin.readline().strip().split()
    if c[0] == "push" : 
        deq.append(c[1])
    elif c[0] == "pop" : 
        if deq : 
            print(deq.pop())
        else : print(-1)
    elif c[0] == "size" : 
        print(len(deq))
    elif c[0] == "empty" : 
        print(1 if len(deq) == 0 else 0)
    else : 
        print(deq[-1] if len(deq) != 0 else -1)
