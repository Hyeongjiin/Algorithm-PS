import sys

sys = sys.stdin.readline

N = int(input())
data = [(0, 0, 0)]
dp = [0] * (N + 2)

for i in range(1, N + 1):
  T, P = map(int, input().split())
  data.append((i, T, P))

for i in range(1, N + 1):
  dp[i] = max(dp[i], dp[i - 1])
  if i + data[i][1] <= N + 1:
    dp[i + data[i][1]] = max(dp[i + data[i][1]], dp[i] + data[i][2])

print(max(dp))