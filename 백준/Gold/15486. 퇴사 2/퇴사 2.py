import sys

sys = sys.stdin.readline

N = int(input())
dp = [0] * (N + 2)
answer = 0

for i in range(1, N + 1):
  T, P = map(int, input().split())
  dp[i] = max(dp[i], dp[i - 1])
  if i + T <= N + 1:
    dp[i + T] = max(dp[i + T], dp[i] + P)
  answer = max(answer, dp[i])
answer = max(answer, dp[N + 1])
print(answer)