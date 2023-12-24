import sys

input = sys.stdin.readline

INF = int(1e9)
graph = [[INF] * 64 for _ in range(64)]
for i in range(64):
  graph[i][i] = 0
N = int(input())
for i in range(N):
  a = input().strip().split(" => ")
  if a[0] == a[1]:
    continue
  graph[ord(a[0]) - 65][ord(a[1]) - 65] = 1

for k in range(64):
  for i in range(64):
    for j in range(64):
      graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

answer = []
for i in range(64):
  for j in range(64):
    if graph[i][j] > 0 and graph[i][j] < INF:
      answer.append((chr(i + 65), chr(j + 65)))

answer.sort(key = lambda x:(x[0], x[1]))
print(len(answer))
for i in answer:
  print(f"{i[0]} => {i[1]}")