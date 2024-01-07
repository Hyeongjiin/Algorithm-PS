import sys

input = sys.stdin.readline

def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, x, y):
  x = find_parent(parent, x)
  y = find_parent(parent, y)
  if x != y:
    parent[y] = x

N, M = map(int, input().split())
parent = [0] * (N + 1)
for i in range(N + 1):
  parent[i] = i

for i in range(M):
  mode, a, b = map(int, input().split())
  if mode == 0:
    union_parent(parent, a, b)
  else:
    find_parent(parent, a)
    find_parent(parent, b)
    if parent[a] == parent[b]:
      print("YES")
    else:
      print("NO")