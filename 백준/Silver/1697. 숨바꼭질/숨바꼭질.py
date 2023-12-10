from collections import deque
import sys

def bfs(road, N, K):
  pay = 0
  q = deque([(N, pay)])
  road[N] = pay
  while q:
    current = q.popleft()
    position = current[0]
    pay = current[1] + 1
    if position + 1 <= 100000:
      np = position + 1
      if road[np] != 0 and road[np] > pay:
        road[np] = pay
        q.append((np, pay))
      if road[np] == 0:
        road[np] = pay
        q.append((np, pay))
    if position - 1 >= 0:
      np = position - 1
      if road[np] != 0 and road[np] > pay:
        road[np] = pay
        q.append((np, pay))
      if road[np] == 0:
        road[np] = pay
        q.append((np, pay))
    if position * 2 <= 100000:
      np = position * 2
      if road[np] != 0 and road[np] > pay:
        road[np] = pay
        q.append((np, pay))
      if road[np] == 0:
        road[np] = pay
        q.append((np, pay))
    
input = sys.stdin.readline

N, K = map(int, input().split())
road = [0] * 100001
bfs(road, N, K)
if N == K:
  print(0)
else:
  print(road[K])