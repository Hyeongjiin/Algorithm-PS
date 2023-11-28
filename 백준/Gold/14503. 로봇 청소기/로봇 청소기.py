import sys

input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
ways = [(-1, 0), (0, 1), (1, 0), (0, -1)]
room = []
for i in range(N):
  room.append(list(map(int, input().split())))

count = 0

while True:
  if room[r][c] == 0:
    room[r][c] = -1
    count += 1
  if room[r + 1][c] == 0 or room[r - 1][c] == 0 or room[r][c + 1] == 0 or room[r][c - 1] == 0:
    d -= 1
    if d == -1:
      d = 3
    nr = r + ways[d][0]
    nc = c + ways[d][1]
    if nr < 0 or nr >= N or nc < 0 or nc >= M:
      continue
    if room[nr][nc] == 0:
      r = nr
      c = nc
  else:
    nr = r - ways[d][0]
    nc = c - ways[d][1]
    if nr < 0 or nr >= N or nc < 0 or nc >= M:
      break
    if room[nr][nc] == 1:
      break
    else:
      r = nr
      c = nc
  
print(count)