import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(graph, visited, R):
  visited[R] = 1
  result.append(R)
  for i in graph[R]:
    if visited[i] == 0:
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
result = []
dfs(graph, visited, R)
order = [0] * (N + 1)
for i in range(len(result)):
  order[result[i]] = i + 1

for i in range(1, N + 1):
  print(order[i])