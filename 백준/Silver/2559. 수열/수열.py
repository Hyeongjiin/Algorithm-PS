import sys

input = sys.stdin.readline

N, M = map(int, input().split())
data = list(map(int, input().split()))
target = sum(data[:M])
answer = target
for i in range(M, N):
  target -= data[i - M]
  target += data[i]
  answer = max(answer, target)
print(answer)