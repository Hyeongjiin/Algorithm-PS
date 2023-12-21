import sys

input = sys.stdin.readline

N = int(input())
tri = []
for i in range(N):
  nums = list(map(int, input().split()))
  tri.append(nums)
  
for i in range(1, N):
  for j in range(len(tri[i])):
    if j == 0:
      tri[i][j] = tri[i][j] + tri[i - 1][j]
    elif j  == len(tri[i]) - 1:
      tri[i][j] = tri[i][j] + tri[i - 1][j - 1]
    else:
      tri[i][j] = max(tri[i][j] + tri[i - 1][j - 1], tri[i][j] + tri[i - 1][j])

answer = max(tri[N - 1])
print(answer)