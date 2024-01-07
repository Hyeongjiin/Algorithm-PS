import sys
input = sys.stdin.readline

def triple(x, y, scale):
  if scale == 3:
    for i in range(scale):
      for j in range(scale):
        if i == 1 and j == 1:
          continue
        stars[x + i][y + j] = '*'
  else:
    scale //= 3
    triple(x, y, scale)
    triple(x, y + scale, scale)
    triple(x, y + 2 * scale, scale)
    triple(x + scale, y, scale)
    triple(x + scale, y + 2 * scale, scale)
    triple(x + 2 * scale, y, scale)
    triple(x + 2 * scale, y + scale, scale)
    triple(x + 2 * scale, y + 2 * scale, scale)

N = int(input())
if N == 1:
  print('*')
else:
  stars = [[' '] * N for _ in range(N)]
  triple (0, 0, N)
  for i in range(N):
    for j in range(N):
      print(stars[i][j], end = "")
    print()