from collections import deque
from inspect import stack
import sys

N = int(sys.stdin.readline().rstrip())

stack = deque()

for _ in range(N):
    command = sys.stdin.readline().split()
    if len(command) == 2:
        if command[0] == "push":
            stack.append(command[1])
    else:
        opcode = command[0]
        if opcode == "pop":
            if stack:
                print(stack.pop())
            else:
                print(-1)
        elif opcode == "size":
            print(len(stack))
        elif opcode == "empty":
            if stack:
                print(0)
            else:
                print(1)
        elif opcode == "top":
            if stack:
                print(stack[-1])
            else:
                print(-1)
