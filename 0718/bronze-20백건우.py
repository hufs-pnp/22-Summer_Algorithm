def desolve_sum(n):
    desolve_sums = []
    k = len(str(n))*9
    if n-k > 1:
        start = n-k
    else:
        start = 1
    for x in range(start,n+1):
        if x + sum(map(int, list(str(x)))) == n:
            if not desolve_sums:
                desolve_sums.append(x)
            else:
                if desolve_sums[0] > x:
                    desolve_sums.insert(0,x)
                else:
                    desolve_sums.append(x)
    return desolve_sums

n = int(input())
answer = desolve_sum(n)
if answer:
    print(answer[0])
else:
    print(0)
