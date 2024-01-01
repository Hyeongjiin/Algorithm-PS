import sys

input = sys.stdin.readline

N, M = map(int, input().split())
data = list(map(int, input().split()))
if M == 1:
  print(max(data))
else:
  sum = [0] * N
  sum[0] = data[0]
  answer = -1000000000
  for i in range(1, N):
    sum[i] = sum[i - 1] + data[i]
    if i == M - 1:
      answer = max(answer, sum[i])
    if i > M - 1:
      sum[i] -= data[i - M]
      answer = max(answer, sum[i])
  print(answer)
