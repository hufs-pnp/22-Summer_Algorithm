import sys
input = sys.stdin.readline()

sticks = list(map(int, input.split()))
answer = [1, 2, 3, 4, 5]

while sticks != answer:
    for i in range(4):
        if sticks[i] >= sticks[i + 1]:
            sticks[i], sticks[i + 1] = sticks[i + 1], sticks[i]
            print(" ".join(map(str, sticks)))
