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

while True:
  N, M = map(int, input().split())
  if N == 0 and M == 0:
    break
  parent = [0] * N
  for i in range(1, N):
    parent[i] = i
  
  datas = []
  for i in range(M):
    a, b, cost = map(int, input().split())
    datas.append((cost, a, b))
    
  datas.sort()
  total = 0
  result = 0
  maxi = 0
  for data in datas:
    total += data[0]
    if find_parent(parent, data[1]) != find_parent(parent, data[2]):
      result += data[0]
      union_parent(parent, data[1], data[2])
  
  print(total - result)