import sys
input = sys.stdin.readline

def find_parent(parent, x):
  while parent[x] != x:
    x = parent[x]
  return x

def union_parent(parent, x, y):
  x = find_parent(parent, x)
  y = find_parent(parent, y)
  if x != y:
    parent[y] = x

N, M = map(int, input().split())
parent = [0] * N
for i in range(1, N):
  parent[i] = i

count = 0
flag = 0
for i in range(M):
  a, b = map(int, input().split())
  count += 1
  if find_parent(parent, a) == find_parent(parent, b):
    flag = 1
    break
  else:
    union_parent(parent, a, b)


if flag == 0:
  print(0)
else:
  print(count)