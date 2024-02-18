import sys

input = sys.stdin.readline

N, M = map(int, input().split())
data = list(map(int, input().split()))
for i in range(1, N):
  data[i] += data[i - 1]

for _ in range(M):
  start, end = map(int, input().split())
  if start >= 2:
    print(data[end - 1] - data[start -  2])
  else:
    print(data[end - 1])