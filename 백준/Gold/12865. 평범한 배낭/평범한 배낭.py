import sys
input = sys.stdin.readline
N, K = map(int, input().split())
data = [(0, 0)]
for i in range(N):
    W, V = map(int, input().split())
    data.append((W, V))
dp = [[0] * (K + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    weight = data[i][0]
    value = data[i][1]
    for j in range(1, K + 1):
        if j < weight:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)
print(max(dp[N]))