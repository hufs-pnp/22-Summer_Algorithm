import sys
input = sys.stdin.readline()

D, H, W = map(int, input.split())

x = ( D ** 2 / (H ** 2 + W ** 2)) ** 0.5

height = int(H * x)
weight = int(W * x)

print(f"{height} {weight}")
