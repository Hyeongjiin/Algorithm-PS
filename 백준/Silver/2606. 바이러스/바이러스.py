import sys

input = sys.stdin.readline

def dfs(cpus, visited, v, result):
  visited[v] = True
  result.append(v)
  for i in cpus[v]:
    if not visited[i]:
      dfs(cpus, visited, i, result)
    
N = int(input())
M = int(input())
cpus = [[] for _ in range(N + 1)]
for i in range(M):
  start, end = map(int, input().split())
  cpus[start].append(end)
  cpus[end].append(start)

visited = [False] * (N + 1)
result = []
dfs(cpus, visited, 1, result)
print(len(result) - 1)