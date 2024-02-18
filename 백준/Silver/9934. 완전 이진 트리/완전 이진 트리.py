import sys

input = sys.stdin.readline
N = int(input())
data = list(map(int, input().split()))

result = [[] for _ in range(N)]
for i in range(N):
  for j in range(2 ** i - 1, len(data), 2 ** (i + 1)):
    result[i].append(data[j])

for i in range(len(result) - 1, -1, -1):
  print(*result[i])