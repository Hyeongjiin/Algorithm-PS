import sys

def dfs(cur_v, cost):
  if distance[cur_v] != INF:
    return
  distance[cur_v] = cost
  for nxt_v, nxt_cost in tree[cur_v]:
    dfs(nxt_v, cost + nxt_cost)
      
INF = int(10e12)
N = int(input())
tree = [[] for _ in range(N + 1)]
for i in range(N):
  data = list(map(int, input().split()))
  v = data[0]
  for j in range(1, len(data) - 1, 2):
    tree[v].append((data[j], data[j + 1]))

distance = [INF] * (N + 1)
dfs(1, 0)
idx = 0
maxi = 0
for i in range(1, N + 1):
  if distance[i] > maxi:
    maxi = distance[i]
    idx = i
distance = [INF] * (N + 1)
dfs(idx, 0)
ans = 0
for i in range(1, N + 1):
  if distance[i] > ans:
    ans = distance[i]
print(ans)
    