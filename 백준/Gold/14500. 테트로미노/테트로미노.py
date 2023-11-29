import sys
input = sys.stdin.readline

N, M = map(int, input().split())
space = []
for i in range(N):
  space.append(list(map(int, input().split())))
maxi = 0
result = 0

for x in range(N):
  for y in range(M):
    # 1-1
    if y + 3 < M:
      result = space[x][y] + space[x][y + 1] + space[x][y + 2] + space[x][y + 3]
      maxi = max(maxi, result)
    # 1-2
    if x + 3 < N:
      result = space[x][y] + space[x + 1][y] + space[x + 2][y] + space[x + 3][y]
      maxi = max(maxi, result)
    # 2
    if x + 1 < N and y + 1 < M:
      result = space[x][y] + space[x][y + 1] + space[x + 1][y] + space[x + 1][y + 1]
      maxi = max(maxi, result)
    # 3-1
    if x + 2 < N and y + 1 < M:
      result = space[x][y] + space[x + 1][y] + space[x + 2][y] + space[x + 2][y + 1]
      maxi = max(maxi, result)
    # 3-2
    if x + 2 < N and y - 1 >= 0:
      result = space[x][y] + space[x + 1][y] + space[x + 2][y] + space[x + 2][y - 1]
      maxi = max(maxi, result)
    # 3-3
    if x - 1 >= 0 and y + 2 < M:
      result = space[x][y] + space[x][y + 1] + space[x][y + 2] + space[x - 1][y + 2]
      maxi = max(maxi, result)
    # 3-4
    if x - 1 >= 0 and y + 2 < M:
      result = space[x][y] + space[x][y + 1] + space[x][y + 2] + space[x - 1][y]
      maxi = max(maxi, result)
    # 3-5
    if x + 2 < N and y + 1 < M:
      result = space[x][y] + space[x][y + 1] + space[x + 1][y + 1] + space[x + 2][y + 1]
      maxi = max(maxi, result)
    # 3-6
    if x + 2 < N and y + 1 < M:
      result = space[x][y] + space[x][y + 1] + space[x + 1][y] + space[x + 2][y]
      maxi = max(maxi, result)
    # 3-7
    if x + 1 < N and y + 2 < M:
      result = space[x][y] + space[x][y + 1] + space[x][y + 2] + space[x + 1][y]
      maxi = max(maxi, result)
    # 3-8
    if x + 1 < N and y + 2 < M:
      result = space[x][y] + space[x][y + 1] + space[x][y + 2] + space[x + 1][y + 2]
      maxi = max(maxi, result)
    # 4-1
    if x + 2 < N and y + 1 < M:
      result = space[x][y] + space[x + 1][y] + space[x + 1][y + 1] + space[x + 2][y + 1]
      maxi = max(maxi, result)
    # 4-2
    if x + 2 < N and y - 1 >= 0:
      result = space[x][y] + space[x + 1][y] + space[x + 1][y - 1] + space[x + 2][y - 1]
      maxi = max(maxi, result)
    # 4-3
    if x + 1 < N and y - 1 >= 0 and y + 1 < M:
      result = space[x][y] + space[x][y + 1] + space[x + 1][y] + space[x + 1][y - 1]
      maxi = max(maxi, result)
    # 4-4
    if x + 1 < N and y + 2 < M:
      result = space[x][y] + space[x][y + 1] + space[x + 1][y + 1] + space[x + 1][y + 2]
      maxi = max(maxi, result)
    # 5-1
    if x + 1 < N and y + 2 < M:
      result = space[x][y] + space[x][y + 1] + space[x][y + 2] + space[x + 1][y + 1]
      maxi = max(maxi, result)
    # 5-2
    if x + 2 < N and y + 1 < M:
      result = space[x][y] + space[x + 1][y] + space[x + 2][y] + space[x + 1][y + 1]
      maxi = max(maxi, result)
    # 5-3 
    if x + 2 < N and y - 1 >= 0:
      result = space[x][y] + space[x + 1][y] + space[x + 2][y] + space[x + 1][y - 1]
      maxi = max(maxi, result)
    # 5-4
    if x - 1 >= 0 and y + 2 < M:
      result = space[x][y] + space[x][y + 1] + space[x][y + 2] + space[x - 1][y + 1]
      maxi = max(maxi, result)
print(maxi)