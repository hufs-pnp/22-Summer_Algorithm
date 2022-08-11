station = []

for _ in range(4):
    in_out = list(map(int ,input().split()))
    station.append(in_out)

current, max = station[0][1], station[0][1]

for i in range(1, 4):
    current -= station[i][0]
    current += station[i][1]
    if current >= max:  max = current
    
print(max)
