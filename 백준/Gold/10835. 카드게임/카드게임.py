import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
dp = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(N - 1, -1, -1):
  for j in range(N - 1, -1, -1):
    if A[i] > B[j]:
      dp[i][j] = max(dp[i][j + 1] + B[j], dp[i + 1][j], dp[i + 1][j + 1])
    else:
      dp[i][j] = max(dp[i + 1][j], dp[i + 1][j + 1])

print(dp[0][0])