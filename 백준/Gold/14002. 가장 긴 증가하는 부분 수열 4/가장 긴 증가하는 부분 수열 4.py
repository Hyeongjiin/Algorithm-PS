import sys
input = sys.stdin.readline
N = int(input())
data = list(map(int, input().split()))
dp = [0] * N
for i in range(1, N):
  for j in range(i):
    if data[j] < data[i]:
      dp[i] = max(dp[i], dp[j] + 1)

result = max(dp)
count = result
print(count + 1)
answer = []
for i in range(N - 1, -1, -1):
  if dp[i] == count:
    answer.append(data[i])
    count -= 1

for i in range(result, -1, -1):
  print(answer[i], end = " ")