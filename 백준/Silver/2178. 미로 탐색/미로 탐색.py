from collections import deque
import sys

def bfs(y, x, cnt):
    queue = deque()
    queue.append((y, x, cnt))
    while queue:
        y, x, cnt = queue.popleft()
        if y < 0 or x < 0 or y >= N or x >= M:
            continue
        if y == N - 1 and x == M - 1:
            cnt += 1
            return cnt
        if graph[y][x] == 1:
            cnt += 1
            graph[y][x] = -1
            queue.append((y + 1, x, cnt))
            queue.append((y - 1, x, cnt))
            queue.append((y, x + 1, cnt))
            queue.append((y, x - 1, cnt))

N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))

result = bfs(0, 0, 0)
print(result)