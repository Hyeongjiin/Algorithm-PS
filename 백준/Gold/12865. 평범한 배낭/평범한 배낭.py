import sys

input = sys.stdin.readline

N, K = map(int, input().split())
datas = []
for _ in range(N):
  datas.append(tuple(map(int, input().split())))
dp = [0] * (K + 1)

for data in datas:
  w, v = data
  for i in range(K, w-1, -1):
    dp[i] = max(dp[i], dp[i - w] + v)

print(dp[K])