import sys

input = sys.stdin.readline

def find_parents(parents, x):
  if parents[x] != x:
    parents[x] = find_parents(parents, parents[x])
  return parents[x]

def union_parents(parents, x, y):
  x = find_parents(parents, x)
  y = find_parents(parents, y)
  if x != y:
    parents[y] = x

N = int(input())
x = []
y = []
z = []
for idx in range(N):
  px, py, pz = map(int, input().split())
  x.append((px, idx))
  y.append((py, idx))
  z.append((pz, idx))

x.sort()
y.sort()
z.sort()

costs = []
for i in range(1, N):
  costx = x[i][0] - x[i - 1][0]
  ux = x[i][1]
  vx = x[i - 1][1]
  costs.append((costx, ux, vx))
  costy = y[i][0] - y[i - 1][0]
  uy = y[i][1]
  vy = y[i - 1][1]
  costs.append((costy, uy, vy))
  costz = z[i][0] - z[i - 1][0]
  uz = z[i][1]
  vz = z[i - 1][1]
  costs.append((costz, uz, vz))

costs.sort()

parents = [i for i in range(N)]
count = 0
answer = 0

for cost, u, v in costs:
  if find_parents(parents, u) != find_parents(parents, v):
    union_parents(parents, u, v)
    count += 1
    answer += cost
    if count == N - 1:
      break

print(answer)