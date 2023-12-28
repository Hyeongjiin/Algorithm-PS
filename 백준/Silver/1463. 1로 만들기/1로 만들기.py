import sys
input = sys.stdin.readline
N = int(input())
data = [0] * (N + 1)
for i in range(2, N + 1):
    data[i] = data[i - 1] + 1
    if i % 2 == 0:
        data[i] = min(data[i], data[i // 2] + 1)
    if i % 3 == 0:
        data[i] = min(data[i], data[i // 3] + 1)
print(data[N])