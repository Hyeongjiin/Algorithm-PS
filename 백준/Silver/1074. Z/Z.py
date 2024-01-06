import sys
input = sys.stdin.readline
def Z(x, y, scale):
  global result
  if x <= r <= x + scale - 1 and y <= c <= y + scale - 1:
    if scale == 2:
      if x <= r <= x + 1 and y <= c <= y + 1:
        for i in range(scale):
          for j in range(scale):
            result += 1
            if x + i == r and y + j == c:
              print(result - 1)
              sys.exit()
    else:
      scale //= 2
      Z(x, y, scale)
      Z(x, y + scale, scale)
      Z(x + scale, y, scale)
      Z(x + scale, y + scale, scale)
  else:
    result += scale ** 2

N, r, c = map(int, input().split())
N = 2**N
global result
result = 0
Z(0, 0, N)