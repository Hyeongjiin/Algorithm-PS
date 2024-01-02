from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e9)
def bfs(start, floors):
  q = deque([start])
  floors[start] = 0
  visited[start] = True
  while q:
    current = q.popleft()
    if current + U <= F and visited[current + U] == False:
      floors[current + U] = min(floors[current] + 1, floors[current + U])
      visited[current + U] = True
      q.append(current + U)
    if current - D > 0 and visited[current - D] == False:
      floors[current - D] = min(floors[current] + 1, floors[current - D])
      visited[current - D] = True
      q.append(current - D)
    
F, S, G, U, D = map(int, input().split())
# F - 총 층계 S - 강호가 있는 곳  G - 목표 층  U - 위로 층 이동  D - 아래 층 이동
floors = [INF] * (F + 1)
visited = [False] * (F + 1)
bfs(S, floors)
if floors[G] == INF:
  print("use the stairs")
else:
  print(floors[G])