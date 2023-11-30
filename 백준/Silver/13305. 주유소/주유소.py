N = int(input())
roads = list(map(int, input().split()))
citys = list(map(int, input().split()))

data = [(citys[0], 0)]
standard = citys[0]
charge = 0
for i in range(1, N - 1):
    if standard > citys[i]:
        standard = citys[i]
        data.append((standard, i))
data.append((citys[-1], N - 1))
start = 0
for i in range(len(data) - 1):
    for j in range(start, data[i + 1][1]):
        charge += data[i][0] * roads[j]
    start = data[i + 1][1]
print(charge)