import sys
input = sys.stdin.readline
INF = int(1e9)
N, M = map(int, input().split())
city = [[INF] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
  city[i][i] = 0
for i in range(M):
  start, end = map(int, input().split())
  city[start][end] = 1
  city[end][start] = 1
for k in range(1, N + 1):
  for i in range(1, N + 1):
    for j in range(1, N + 1):
      city[i][j] = min(city[i][j], city[i][k] + city[k][j])
case = []
for i in range(1, N + 1):
  for j in range(1, N + 1):
    if i == j:
      continue
    case.append((i, j))

answer = []
result = INF
for i in case:
  F = i[0]
  S = i[1]
  total = 0
  for j in range(1, N + 1):
    total += min(city[F][j], city[S][j])
  if total < result:
    result = total
    answer = [i]

print(answer[0][0], answer[0][1], 2 * result)