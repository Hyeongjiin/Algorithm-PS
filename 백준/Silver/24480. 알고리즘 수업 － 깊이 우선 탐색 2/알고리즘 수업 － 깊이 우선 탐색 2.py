import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(graph, visited, R):
  global count
  visited[R] = count
  for i in graph[R]:
    if visited[i] == 0:
      count += 1
      dfs(graph, visited, i)
  
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
  start, end = map(int, input().split())
  graph[start].append(end)
  graph[end].append(start)

for i in range(1, N + 1):
  graph[i].sort(reverse=True)

visited = [0] * (N + 1)
count = 1
dfs(graph, visited, R)
for i in range(1, N + 1):
  print(visited[i])