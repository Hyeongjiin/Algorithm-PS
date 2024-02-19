import sys

input = sys.stdin.readline

N = int(input())
points = []
for _ in range(N):
  points.append(tuple(map(int, input().split())))

distance = []
for i in range(1, N):
  distance.append(abs(points[i][0] - points[i - 1][0]) + abs(points[i][1] - points[i - 1][1]))

distanceE = []
for i in range(2, N):
  distanceE.append(abs(points[i][0] - points[i - 2][0]) + abs(points[i][1] - points[i - 2][1]))

answer = sum(distance)
max_diff = 0

for i in range(len(distanceE)):
  diff = distance[i] + distance[i + 1] - distanceE[i]
  if diff > max_diff:
    max_diff = diff
answer -= max_diff
print(answer)