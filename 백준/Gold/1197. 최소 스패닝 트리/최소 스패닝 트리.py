from collections import deque
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
data = []
for _ in range(M):
  u, v, cost = map(int, input().split())
  data.append((cost, u, v))

parent = [0] * (N + 1)
for i in range(1, N + 1):
  parent[i] = i

data.sort()

answer = 0
count = 0
for i in data:
  if find_parent(parent, i[1]) != find_parent(parent, i[2]):
    union_parent(parent, i[1], i[2])
    answer += i[0]
    count += 1
  if count == N - 1:
    break

print(answer)