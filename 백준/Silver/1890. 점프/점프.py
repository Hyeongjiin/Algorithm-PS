import sys

sys = sys.stdin.readline

N = int(input())
board = []
for _ in range(N):
  board.append(list(map(int, input().split())))

dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
  for j in range(N):
    if i == N - 1 and j == N - 1:
      continue
    dist = board[i][j]
    if i + dist < N:
      dp[i + dist][j] += dp[i][j]
    if j + dist < N:
      dp[i][j + dist] += dp[i][j]

print(dp[N - 1][N - 1])