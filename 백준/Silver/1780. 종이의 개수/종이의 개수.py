import sys

input = sys.stdin.readline


def triple(x, y, scale):
  global mone
  global zero
  global one
  base = paper[x][y]
  flag = 0
  for i in range(scale):
    if flag == 1:
      break
    for j in range(scale):
      if base != paper[x + i][y + j]:
        flag = 1
        break
  if flag == 0:
    if base == -1:
      mone += 1
    elif base == 0:
      zero += 1
    else:
      one += 1
    return
  else:
    scale //= 3
    triple(x, y, scale)
    triple(x, y + scale, scale)
    triple(x, y + 2 * scale, scale)
    triple(x + scale, y, scale)
    triple(x + scale, y + scale, scale)
    triple(x + scale, y + 2 * scale, scale)
    triple(x + 2 * scale, y, scale)
    triple(x + 2 * scale, y + scale, scale)
    triple(x + 2 * scale, y + 2 * scale, scale)


N = int(input())
paper = []
for _ in range(N):
  paper.append(list(map(int, input().rstrip().split())))

global mone
mone = 0
global zero
zero = 0
global one
one = 0

triple(0, 0, N)
print(mone)
print(zero)
print(one)