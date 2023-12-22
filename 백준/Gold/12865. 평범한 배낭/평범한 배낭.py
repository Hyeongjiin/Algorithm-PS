import sys
input = sys.stdin.readline
N, K = map(int, input().split())
items = [(0, 0)]
for i in range(N):
  items.append(tuple(map(int, input().split())))

dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
  weight = items[i][0]
  value = items[i][1]
  for j in range(1, K + 1):
    if weight > j:
      dp[i][j] = dp[i - 1][j]
    else:
      dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)

print(dp[N][K])
