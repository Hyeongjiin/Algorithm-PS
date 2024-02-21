from collections import deque
import sys

input = sys.stdin.readline


def bfs():
  q = deque()
  q.append(locations[0])
  visited[0] = True
  while q:
    if visited[N + 1] == True:
      return True
    cur_x, cur_y = q.popleft()
    for i in range(1, N + 2):
      if visited[i] == True:
        continue
      distance = abs(locations[i][0] - cur_x) + abs(locations[i][1] - cur_y)
      if distance > 1000:
        continue
      else:
        visited[i] = True
        q.append((locations[i][0], locations[i][1]))
  return False


T = int(input())
for _ in range(T):
  N = int(input())
  visited = [False] * (N + 2)
  locations = []
  for _ in range(N + 2):
    locations.append(tuple(map(int, input().rstrip().split())))
  answer = bfs()
  if answer:
    print('happy')
  else:
    print('sad')
