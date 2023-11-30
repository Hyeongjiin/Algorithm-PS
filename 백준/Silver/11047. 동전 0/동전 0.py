import sys

input = sys.stdin.readline

N, K = map(int, input().split())
coins = []
for i in range(N):
  coins.append(int(input()))
coins.sort(reverse=True)
result = 0
for coin in coins:
  result += K // coin
  K %= coin
print(result)