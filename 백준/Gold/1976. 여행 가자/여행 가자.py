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

N = int(input())
M = int(input())
parent = [0] * N
for i in range(1, N):
  parent[i] = i
for i in range(N):
  data = list(map(int, input().split()))
  for j in range(N):
    if i == j:
      continue
    if data[j] == 1:
      union_parent(parent, i, j)

for i in range(N):
  find_parent(parent, i)
  
visit = list(map(int, input().split()))
p = parent[visit[0] - 1]
result = 0

for i in visit:
  if parent[i - 1] != p:
    result = 1

if result == 1:
  print("NO")
else:
  print("YES")