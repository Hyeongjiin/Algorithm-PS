import sys
input = sys.stdin.readline
N = int(input())
info = list(map(int, input().split()))
result = [0] * N
for idx, data in enumerate(info, 1):
  for i in range(N):
    if result[i] == 0:
      if data == 0:
        result[i] = idx
        break
      else:
        data -= 1
print(*result)