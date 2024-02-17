from collections import deque
import sys

input = sys.stdin.readline
INF = int(1e9)

def bfs(idx):
  q = deque()
  q.append(idx)
  visited[idx] = True

  while q:
    cur_p = q.popleft()
    i = 1
    while True:
      nIdx = cur_p + data[cur_p] * i
      if nIdx >= N:
        break
      if visited[nIdx] == False:
        visited[nIdx] = True
        distance[nIdx] = distance[cur_p] + 1
        q.append(nIdx)
      i += 1

    i = 1
    while True:
      nIdx = cur_p - data[cur_p] * i
      if nIdx < 0:
        break
      if visited[nIdx] == False:
        visited[nIdx] = True
        distance[nIdx] = distance[cur_p] + 1
        q.append(nIdx)
      i += 1

  

N = int(input())
data = list(map(int, input().split()))
start, end = map(int, input().split())
start -= 1
end -= 1

visited = [False] * N
distance = [-1] * N
distance[start] = 0
bfs(start)
print(distance[end])