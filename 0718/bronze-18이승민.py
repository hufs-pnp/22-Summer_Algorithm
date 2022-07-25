N = int(input())

case = 0

for i in range(1, N+1):
    li = list(map(int, str(i)))
    answer = i + sum(li)

    if answer == N:
        print(i)
        case = 1
        break

if case == 0:
    print(0)
