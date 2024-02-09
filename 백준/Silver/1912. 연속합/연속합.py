import sys

input = sys.stdin.readline
INF = -int(10e9)
N = int(input())
data = list(map(int, input().split()))
dp = [INF] * N
dp[0] = data[0]
for i in range(1, N):
  dp[i] = max(dp[i - 1] + data[i], data[i])
print(max(dp))
