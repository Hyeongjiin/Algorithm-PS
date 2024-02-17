from collections import deque
import sys

input = sys.stdin.readline


def bfs(coin):
  coin_p = deque()
  coin_p.append((coin[0], coin[1], coin[2], coin[3], 0))
  while coin_p:
    x1, y1, x2, y2, count = coin_p.popleft()
    if count >= 10:
      return -1
    for move in moves:
      nx1 = x1 + move[0]
      ny1 = y1 + move[1]
      nx2 = x2 + move[0]
      ny2 = y2 + move[1]
      if 0 <= nx1 < N and 0 <= nx2 < N and 0 <= ny1 < M and 0 <= ny2 < M:
        if board[nx1][ny1] == '#':
          nx1 = x1
          ny1 = y1
        if board[nx2][ny2] == '#':
          nx2 = x2
          ny2 = y2
        coin_p.append((nx1, ny1, nx2, ny2, count + 1))
      elif (nx1 < 0 or nx1 >= N or ny1 < 0 or ny1 >= M) and (nx2 < 0 or nx2 >= N or ny2 < 0 or ny2 >= M):
        continue
      else:
        return count + 1


N, M = map(int, input().split())
board = []
for _ in range(N):
  board.append(list(input().rstrip()))

moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visited = {}
coin = []
for i in range(N):
  for j in range(M):
    if board[i][j] == "o":
      coin.append(i)
      coin.append(j)
result = bfs(coin)
print(result)