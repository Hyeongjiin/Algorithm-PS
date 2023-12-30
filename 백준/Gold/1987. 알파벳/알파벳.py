import sys

def dfs(visited, depth, x, y):
  global dist
  dist = max(dist, depth)
  chr = board[x][y]
  visited[ord(chr) - 65] = True
  moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
  for move in moves:
    nx = x + move[0]
    ny = y + move[1]
    if nx < 0 or ny < 0 or nx > R - 1 or ny > C - 1:
      continue
    nchr = board[nx][ny]
    if visited[ord(nchr) - 65] == False:
      visited[ord(nchr) - 65] = True
      dfs(visited, depth + 1, nx, ny)
      visited[ord(nchr) - 65] = False
      
input = sys.stdin.readline
R, C = map(int, input().split())
board = []
for i in range(R):
  board.append(list(input().rstrip()))

global dist
dist = 0
visited = [False] * 26
dfs(visited, 1, 0, 0)
print(dist)