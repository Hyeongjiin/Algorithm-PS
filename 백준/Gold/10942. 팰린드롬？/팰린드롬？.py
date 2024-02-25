import sys

input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))

dp = [[0] * N for _ in range(N)]
for i in range(N):
  dp[i][i] = 1

for i in range(N - 1):
  if data[i] == data[i + 1]:
    dp[i][i + 1] = 1

for cnt in range(2, N):
  for i in range(N - cnt):
    j = i + cnt
    if data[i] == data[j] and dp[i + 1][j - 1] == 1:
      dp[i][j] = 1

M = int(input())
for _ in range(M):
  S, E = map(int, input().split())
  print(dp[S - 1][E - 1])
