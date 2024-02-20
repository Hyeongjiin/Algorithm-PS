import sys

input = sys.stdin.readline

N = int(input())
dp = [[1] * 10 for _ in range(1000)]
for i in range(1, 1000):
  for j in range(1, 10):
    dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

print(sum(dp[N - 1]) % 10007)